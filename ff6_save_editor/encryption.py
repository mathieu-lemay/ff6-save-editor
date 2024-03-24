from typing import cast

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from py3rijndael import RijndaelCbc, ZeroPadding  # type: ignore[import-untyped]
from pydantic_settings import BaseSettings, SettingsConfigDict


class EncryptionSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="FF6_EDITOR_", env_file=".env")

    password: bytes
    salt: bytes
    block_size: int = 32


class EncryptionManager:
    def __init__(self, encryption_settings: EncryptionSettings | None = None) -> None:
        encryption_settings = encryption_settings or EncryptionSettings()

        algo = hashes.SHA1()  # noqa: S303: Insecure algorithm. Not my choice.
        kdf = PBKDF2HMAC(algo, length=64, salt=encryption_settings.salt, iterations=10)
        key_iv_bytes = kdf.derive(encryption_settings.password)

        key = key_iv_bytes[: encryption_settings.block_size]
        iv = key_iv_bytes[encryption_settings.block_size :]

        self.cipher = RijndaelCbc(
            key=key,
            iv=iv,
            padding=ZeroPadding(encryption_settings.block_size),
            block_size=encryption_settings.block_size,
        )

    def encrypt(self, data: bytes) -> bytes:
        return cast(bytes, self.cipher.encrypt(data))

    def decrypt(self, data: bytes) -> bytes:
        plaintext = cast(bytes, self.cipher.decrypt(data))
        padding = b"\x00" * (len(data) - len(plaintext))

        return plaintext + padding
