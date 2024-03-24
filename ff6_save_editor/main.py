#! /usr/bin/env python

import sys
import zlib
from pathlib import Path

from ff6_save_editor.encryption import EncryptionManager
from ff6_save_editor.models import SaveModel


def load(src: Path) -> SaveModel:
    buffer = src.read_bytes()

    enc = EncryptionManager()
    decrypted = enc.decrypt(buffer)

    raw = zlib.decompress(decrypted, wbits=-zlib.MAX_WBITS)

    src.with_suffix(".json").write_bytes(raw)

    return SaveModel.model_validate_json(raw)


def save(save: SaveModel, dst: Path) -> None:
    raw = save.model_dump_json()
    buffer = zlib.compress(raw.encode(), wbits=-zlib.MAX_WBITS)

    enc = EncryptionManager()
    buffer = enc.encrypt(buffer)

    dst.write_bytes(buffer)


def main() -> None:
    fp = Path()
    if len(sys.argv) > 1:
        fp /= sys.argv[1]
    else:
        fp /= "sample/ookrbATYovG3tEOXIH4HqWnsv8TrUlRWzM8AlCmW2mk="

    save_data = load(fp)

    dst = fp.with_suffix(fp.suffix + ".new")
    print(f"Saving to {dst}")

    #  for k, v in save_data.user_data.model_dump().items():
    #      print(f"{k} => {v}")

    for c in save_data.user_data.owned_character_list.target:
        if c.name == "Shadow":
            print(f"{c.equipmentList=}")
            print(f"{c.equipmentAbilitys=}")
            print(f"{c.additionOrderOwnedAbilityIds=}")
            print(f"{c.sortOrderOwnedAbilityIds=}")
            print(f"{c.abilityDictionary=}")
            print(f"{c.skillLevelTargets=}")
            print(f"{c.learningAbilitys=}")
            print(f"{c.equipmentAbilitys=}")
            print(f"{c.numberOfButtles=}")
            print(f"{c.ownedMonsterId=}")

    #  save(save_data, dst)

    #  with (Path("sample") / "ookrbATYovG3tEOXIH4HqWnsv8TrUlRWzM8AlCmW2mk=.json").open(
    #      "r"
    #  ) as f:
    #      save = SaveModel.model_validate_json(f.read())
    #
    #  print(save.model_dump_json(indent=2))
    #
    #  with Path("image.png").open("wb") as f:
    #      f.write(b64decode(save.picture_data))


if __name__ == "__main__":
    main()
