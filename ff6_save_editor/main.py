#! /usr/bin/env python

import zlib
from pathlib import Path

from rich import print as rprint
from rich import reconfigure

from ff6_save_editor.encryption import EncryptionManager
from ff6_save_editor.models import SaveModel


def load(src: Path) -> SaveModel:
    buffer = src.read_bytes()

    enc = EncryptionManager()
    decrypted = enc.decrypt(buffer)

    raw = zlib.decompress(decrypted, wbits=-zlib.MAX_WBITS)

    src.with_suffix(".json").write_bytes(raw)

    return SaveModel.model_validate_json(raw)


def save(save_model: SaveModel, dst: Path) -> None:
    raw = save_model.model_dump_json()
    buffer = zlib.compress(raw.encode(), wbits=-zlib.MAX_WBITS)

    enc = EncryptionManager()
    buffer = enc.encrypt(buffer)

    dst.write_bytes(buffer)


def main() -> None:
    # fp = Path()
    # if len(sys.argv) > 1:
    #     fp /= sys.argv[1]
    # else:
    #     fp /= "sample/ookrbATYovG3tEOXIH4HqWnsv8TrUlRWzM8AlCmW2mk="
    #
    # save_data = load(fp)

    with (Path("sample") / "sample.json").open() as f:
        save_data = SaveModel.model_validate_json(f.read())

    reconfigure(color_system="truecolor")
    rprint(f"{save_data.id=}")
    rprint(f"{save_data.timestamp=}")

    for c in save_data.user_data.owned_character_list.target:
        if c.name == "Shadow":
            rprint(c)
            #  print(f"{c.character_status_id=}")
            #  print(f"{c.is_enable_corps=}")
            #  print(f"{c.job_id=}")
            #  print(f"{c.name=}")
            #  print(f"{c.current_exp=}")
            # print(f"{c.parameter=}")
            #  print(f"{c.command_list=}")
            #  print(f"{c.ability_list=}")
            #  print(f"{c.ability_slot_data_list=}")
            #  print(f"{c.job_list=}")
            #  print(f"{c.equipment_list=}")
            #  print(f"{c.addition_order_owned_ability_ids=}")
            #  print(f"{c.sort_order_owned_ability_ids=}")
            #  print(f"{c.ability_dictionary=}")
            #  print(f"{c.skill_level_targets=}")
            #  print(f"{c.learning_abilities=}")
            #  print(f"{c.equipment_abilities_=}")
            #  print(f"{c.number_of_buttles=}")
            #  print(f"{c.owned_monster_id=}")
            #  print(f"{c.magic_stone_id=}")
            #  print(f"{c.magic_learning_value=}")
            #  print(f"{c.is_default_name=}")

    save_data.user_data.owned_character_list.target = []
    rprint(save_data)

    #  dst = fp.with_suffix(fp.suffix + ".new")
    #  print(f"Saving to {dst}")
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
