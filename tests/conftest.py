from collections.abc import Generator
from time import time

import pytest

from ff6_save_editor.encryption import EncryptionSettings


@pytest.fixture(autouse=True)
def faker_seed() -> float:
    return time()


@pytest.fixture(autouse=True, scope="session")
def _disable_encryption_settings_env_file_loading() -> Generator[None, None, None]:
    """Workaround to ensure we're not using values from a .env file."""
    real_value = EncryptionSettings.model_config["env_file"]
    EncryptionSettings.model_config["env_file"] = None
    yield
    EncryptionSettings.model_config["env_file"] = real_value
