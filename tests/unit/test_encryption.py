import pytest
from _pytest.monkeypatch import MonkeyPatch
from faker import Faker

from ff6_save_editor.encryption import EncryptionManager, EncryptionSettings


@pytest.fixture(scope="session")
def encryption_settings() -> EncryptionSettings:
    return EncryptionSettings(
        password=b"Xh+j8rxRhM+n/SSu3rLAEpYCcNV4vdH6",
        salt=b"RPoru8ebLkjoVHA3+9CprAFROjJyQ9hm",
    )


def test_encryption_settings_should_load_values_from_env(
    monkeypatch: MonkeyPatch, faker: Faker
) -> None:
    password = faker.pystr()
    salt = faker.pystr()
    block_size = faker.pyint()

    with monkeypatch.context() as p:
        p.setenv("FF6_EDITOR_ENCRYPTION_PASSWORD", password)
        p.setenv("FF6_EDITOR_ENCRYPTION_SALT", salt)
        p.setenv("FF6_EDITOR_ENCRYPTION_BLOCK_SIZE", str(block_size))
        settings = EncryptionSettings()

    assert settings == EncryptionSettings(
        password=password.encode(), salt=salt.encode(), block_size=block_size
    )


def test_encryption_settings_default_values(faker: Faker) -> None:
    settings = EncryptionSettings(password=faker.pystr(), salt=faker.pystr())

    assert settings.block_size == 32


def test_encryption_manager_encrypt(encryption_settings: EncryptionSettings) -> None:
    value = b"cItYc1GeUcjXH7QMaMR5RI6vIDPrIPKZ"
    expected = (
        b"\xa0#\n\x94\x87\x92&|\xffm\x82\xed\xb5\xe9\xe2r"
        b"%9\xc3\xe9\xf8\x82>\xbdrZ\xa9\xb9\x87\x99R\xc9"
    )

    enc = EncryptionManager(encryption_settings)
    encrypted = enc.encrypt(value)

    assert encrypted == expected

    # Ensure round trip
    assert enc.decrypt(encrypted) == value


def test_encryption_manager_decrypt(encryption_settings: EncryptionSettings) -> None:
    value = b"LW8oL50H9SnzXxF/z8jQKHvkIuTKyoNZ"
    expected = (
        b"\x13\xb9@\x18\xa8U\x03\x83\x0f\xed\tr\x8d\xd0\x9f."
        b"\xbc`\xd3\x84jo\xc2\xb2!\x04\xf8\x9e\xad\x02\xb3\xb5"
    )

    enc = EncryptionManager(encryption_settings)
    decrypted = enc.decrypt(value)

    assert decrypted == expected

    # Ensure round trip
    assert enc.encrypt(decrypted) == value


def test_encryption_manager_produces_different_results_with_other_settings(
    encryption_settings: EncryptionSettings, faker: Faker
) -> None:
    other_password = faker.pystr(min_chars=32, max_chars=32).encode()
    other_salt = faker.pystr(min_chars=32, max_chars=32).encode()
    other_encryption_settings = EncryptionSettings(
        password=other_password, salt=other_salt
    )

    value = faker.pystr(min_chars=32, max_chars=32).encode()

    enc1 = EncryptionManager(encryption_settings)
    enc2 = EncryptionManager(other_encryption_settings)

    encrypted1 = enc1.encrypt(value)
    encrypted2 = enc2.encrypt(value)

    decrypted1 = enc1.decrypt(encrypted1)
    decrypted2 = enc2.decrypt(encrypted2)

    # Both encrypted values should be different
    assert encrypted1 != encrypted2

    # Both should round trip back to the right value
    assert decrypted1 == value
    assert decrypted2 == value

    # Swapping encryptors should _not_ decrypt to the right value
    assert enc1.decrypt(encrypted2) != value
    assert enc2.decrypt(encrypted1) != value
