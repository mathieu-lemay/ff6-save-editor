import json
import sys
import zlib
from datetime import datetime
from pathlib import Path
from typing import Any, Generic, TypeVar, cast

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from py3rijndael import RijndaelCbc, ZeroPadding  # type: ignore[import-untyped]
from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field, field_serializer, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

JsonDict = dict[str, Any]


class EncryptionSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="FF6_EDITOR_")

    password: bytes
    salt: bytes
    block_size: int = 32


class Encryption:
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


class BaseModel(PydanticBaseModel):
    pass


T = TypeVar("T", bound=BaseModel)


class ListWrapper(BaseModel, Generic[T]):
    target: list[T]

    @field_validator("target", mode="before")
    def deserialize_data(cls, v: list[str]) -> list[JsonDict]:
        return [cast(JsonDict, json.loads(i)) for i in v]

    @field_serializer("target")
    def serialize_data(self, items: list[T]) -> list[str]:
        return [i.model_dump_json() for i in items]


class ItemModel(BaseModel):
    content_id: int = Field(alias="contentId")
    count: int


class CharacterModel(BaseModel):
    id: int = Field(alias="id")
    characterStatusId: int = Field(alias="characterStatusId")
    isEnableCorps: bool = Field(alias="isEnableCorps")
    jobId: int = Field(alias="jobId")
    name: str = Field(alias="name")
    currentExp: int = Field(alias="currentExp")
    parameter: str = Field(alias="parameter")
    commandList: str = Field(alias="commandList")
    abilityList: str = Field(alias="abilityList")
    abilitySlotDataList: str = Field(alias="abilitySlotDataList")
    jobList: str = Field(alias="jobList")
    equipmentList: str = Field(alias="equipmentList")
    additionOrderOwnedAbilityIds: str = Field(alias="additionOrderOwnedAbilityIds")
    sortOrderOwnedAbilityIds: str = Field(alias="sortOrderOwnedAbilityIds")
    abilityDictionary: str = Field(alias="abilityDictionary")
    skillLevelTargets: str = Field(alias="skillLevelTargets")
    learningAbilitys: str = Field(alias="learningAbilitys")
    equipmentAbilitys: str = Field(alias="equipmentAbilitys")
    numberOfButtles: int = Field(alias="numberOfButtles")
    ownedMonsterId: int = Field(alias="ownedMonsterId")
    magicStoneId: int = Field(alias="magicStoneId")
    magicLearningValue: int = Field(alias="magicLearningValue")
    isDefaultName: bool = Field(alias="isDefaultName")


class UserData(BaseModel):
    corps_list: str = Field(alias="corpsList")
    corps_slots: str = Field(alias="corpsSlots")
    owned_character_list: ListWrapper[CharacterModel] = Field(
        alias="ownedCharacterList"
    )
    released_jobs: str = Field(alias="releasedJobs")
    owned_gil: int = Field(alias="owendGil")  # sic
    play_time: float = Field(alias="playTime")
    normal_owned_items: ListWrapper[ItemModel] = Field(alias="normalOwnedItemList")
    important_owned_items: str = Field(alias="importantOwendItemList")
    normal_owned_item_sort_id_list: str = Field(alias="normalOwnedItemSortIdList")
    current_area: str = Field(alias="currentArea")
    current_location: str = Field(alias="currentLocation")
    owned_transportations: str = Field(alias="ownedTransportationList")
    owned_crystal_flags: str = Field(alias="owendCrystalFlags")  # sic
    config_data: str = Field(alias="configData")
    warehouse_items: str = Field(alias="warehouseItemList")
    owned_key_items: str = Field(alias="ownedKeyWaordList")  # sic
    owned_magics: str = Field(alias="ownedMagicList")
    learned_abilities: str = Field(alias="learnedAbilityList")
    escape_count: int = Field(alias="escapeCount")
    battle_count: int = Field(alias="battleCount")
    corps_slot_index: int = Field(alias="corpsSlotIndex")
    open_chest_count: int = Field(alias="openChestCount")
    owned_magic_stones: str = Field(alias="ownedMagicStoneList")  # Espers?
    steps: int = Field(alias="steps")
    save_complete_count: int = Field(alias="saveCompleteCount")
    monsters_killed_count: int = Field(alias="monstersKilledCount")
    total_gil: int = Field(alias="totalGil")
    cheat_settings: JsonDict = Field(alias="cheatSettingsData")
    is_opened_game_booster_window: bool = Field(alias="isOpenedGameBoosterWindow")

    @field_validator("normal_owned_items", "owned_character_list", mode="before")
    def deserialize_data(cls, v: str) -> JsonDict:
        return cast(JsonDict, json.loads(v))

    @field_serializer("normal_owned_items", "owned_character_list")
    def serialize_data(self, obj: BaseModel) -> str:
        return obj.model_dump_json()


class SaveModel(BaseModel):
    id: int
    picture_data: str = Field(alias="pictureData")
    user_data: UserData = Field(alias="userData")
    config_data: str = Field(alias="configData")
    data_storage: str = Field(alias="dataStorage")
    map_data: str = Field(alias="mapData")
    timestamp: datetime = Field(alias="timeStamp")
    play_time: float = Field(alias="playTime")
    clear_flag: int = Field(alias="clearFlag")
    is_complete_flag: int = Field(alias="isCompleteFlag")

    @field_validator("user_data", mode="before")
    def deserialize_data(cls, v: str) -> JsonDict:
        return cast(JsonDict, json.loads(v))

    @field_serializer("user_data")
    def serialize_data(self, user_data: UserData) -> str:
        return user_data.model_dump_json()

    @field_validator("timestamp", mode="before")
    def deserialize_timestamp(cls, v: str) -> datetime:
        return datetime.strptime(v, "%m/%d/%Y %I:%M:%S %p")

    @field_serializer("timestamp")
    def serialize_timestamp(self, timestamp: datetime) -> str:
        return timestamp.strftime("%m/%d/%Y %I:%M:%S %p")


def load(src: Path) -> SaveModel:
    buffer = src.read_bytes()

    enc = Encryption()
    decrypted = enc.decrypt(buffer)

    raw = zlib.decompress(decrypted, wbits=-zlib.MAX_WBITS)

    src.with_suffix(".json").write_bytes(raw)

    return SaveModel.model_validate_json(raw)


def save(save: SaveModel, dst: Path) -> None:
    raw = save.model_dump_json()
    buffer = zlib.compress(raw.encode(), wbits=-zlib.MAX_WBITS)

    enc = Encryption()
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
