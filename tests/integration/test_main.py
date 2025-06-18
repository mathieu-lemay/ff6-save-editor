import gzip
import zlib
from pathlib import Path

import pytest
from _pytest.config import Config
from faker import Faker

from ff6_save_editor.encryption import EncryptionManager, EncryptionSettings
from ff6_save_editor.main import load, save
from ff6_save_editor.models import SaveModel


@pytest.fixture(scope="session")
def sample_save_data(pytestconfig: Config) -> SaveModel:
    p = pytestconfig.rootpath / "tests" / "integration" / "samples" / "save.json.gz"
    with gzip.open(p) as f:
        return SaveModel.model_validate_json(f.read())


@pytest.fixture
def encryption_settings(faker: Faker) -> EncryptionSettings:
    password = faker.pystr(min_chars=32, max_chars=32)
    salt = faker.pystr(min_chars=32, max_chars=32)

    return EncryptionSettings(password=password, salt=salt)


@pytest.fixture
def encryption_manager(encryption_settings: EncryptionSettings) -> EncryptionManager:
    return EncryptionManager(encryption_settings)


def test_load_and_save_round_trip(
    sample_save_data: SaveModel,
    encryption_settings: EncryptionSettings,
    tmp_path: Path,
    faker: Faker,
) -> None:
    save_file = tmp_path / faker.pystr()
    save(sample_save_data, save_file, encryption_settings)
    new_save_data = load(save_file, encryption_settings)

    assert new_save_data == sample_save_data


def test_load_mode(
    sample_save_data: SaveModel,
    encryption_settings: EncryptionSettings,
    encryption_manager: EncryptionManager,
    tmp_path: Path,
    faker: Faker,
) -> None:
    save_file = tmp_path / faker.pystr()

    raw_save_data = sample_save_data.model_dump_json(by_alias=True).encode()
    compressed = zlib.compress(raw_save_data, wbits=-zlib.MAX_WBITS)
    encrypted = encryption_manager.encrypt(compressed)
    save_file.write_bytes(encrypted)

    # Should decrypt, decompress and load the model
    new_save_data = load(save_file, encryption_settings)
    assert new_save_data == sample_save_data


def test_save_model(
    sample_save_data: SaveModel,
    encryption_settings: EncryptionSettings,
    encryption_manager: EncryptionManager,
    tmp_path: Path,
    faker: Faker,
) -> None:
    save_file = tmp_path / faker.pystr()

    # Should dump the model, compress and encrypt
    save(sample_save_data, save_file, encryption_settings)

    encrypted = save_file.read_bytes()
    decrypted = encryption_manager.decrypt(encrypted)
    decompressed = zlib.decompress(decrypted, wbits=-zlib.MAX_WBITS)

    assert SaveModel.model_validate_json(decompressed) == sample_save_data
