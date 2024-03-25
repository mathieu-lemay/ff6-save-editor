#! /usr/bin/env python

import zlib
from pathlib import Path

from rich import print as rprint

from ff6_save_editor.encryption import EncryptionManager, EncryptionSettings
from ff6_save_editor.models import EsperId, SaveModel


def load(src: Path, encryption_settings: EncryptionSettings | None = None) -> SaveModel:
    buffer = src.read_bytes()

    enc = EncryptionManager(encryption_settings or EncryptionSettings())
    decrypted = enc.decrypt(buffer)

    raw = zlib.decompress(decrypted, wbits=-zlib.MAX_WBITS)

    return SaveModel.model_validate_json(raw)


def save(
    save_model: SaveModel,
    dst: Path,
    encryption_settings: EncryptionSettings | None = None,
) -> None:
    raw = save_model.model_dump_json(by_alias=True).encode()
    buffer = zlib.compress(raw, wbits=-zlib.MAX_WBITS)

    enc = EncryptionManager(encryption_settings or EncryptionSettings())
    encrypted = enc.encrypt(buffer)
    dst.write_bytes(encrypted)


def main() -> None:  # pragma: no cover
    # fp = Path()
    # if len(sys.argv) > 1:
    #     fp /= sys.argv[1]
    # else:
    #     fp /= "sample/ookrbATYovG3tEOXIH4HqWnsv8TrUlRWzM8AlCmW2mk="
    #
    # save_data = load(fp)

    with (Path("sample") / "sample.json").open() as f:
        save_data = SaveModel.model_validate_json(f.read())

    save_data.user_data.owned_espers.target.append(EsperId.Ragnarok)
    save_data.user_data.owned_espers.target.sort()

    # rprint(save_data.user_data)

    # dst = Path("ookrbATYovG3tEOXIH4HqWnsv8TrUlRWzM8AlCmW2mk=")
    # save(save_data, dst)

    for c in save_data.user_data.owned_character_list.target:
        # if c.name in ("Celes",):
        print(f"< ==== {c.name} ({c.id!r}) ==== >")
        rprint(f"{c.esper_id=}")
        rprint(f"{c.skill_level_targets=}")
        rprint(f"{c.learning_abilities=}")
        rprint(f"{c.sort_order_owned_ability_ids=}")


if __name__ == "__main__":  # pragma: no cover
    main()
