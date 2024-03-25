import json
from datetime import datetime
from typing import Any, Generic, TypeVar, cast

from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict, Field, field_serializer, field_validator

JsonDict = dict[str, Any]


class BaseModel(PydanticBaseModel):
    model_config = ConfigDict(extra="forbid")


M = TypeVar("M", bound=BaseModel)
T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class ModelListWrapper(BaseModel, Generic[M]):
    target: list[M]

    @field_validator("target", mode="before")
    def deserialize_data(cls, v: list[str]) -> list[JsonDict]:
        return [cast(JsonDict, json.loads(i)) for i in v]

    @field_serializer("target")
    def serialize_data(self, items: list[M]) -> list[str]:
        return [i.model_dump_json() for i in items]


class PrimitiveListWrapper(BaseModel, Generic[T]):
    target: list[T]


class ItemModel(BaseModel):
    content_id: int = Field(alias="contentId")
    count: int


class KeyValueList(BaseModel, Generic[K, V]):
    keys: list[K]
    values: list[V]


class CharacterParameterModel(BaseModel):
    current_hp: int = Field(alias="currentHP")
    current_mp: int = Field(alias="currentMP")
    current_mp_count_list: KeyValueList[int, int] = Field(alias="currentMpCountList")
    additional_max_mp_count_list: KeyValueList[int, int] = Field(
        alias="addtionalMaxMpCountList"
    )
    additional_level: int = Field(alias="addtionalLevel")
    additional_max_hp: int = Field(alias="addtionalMaxHp")
    additional_max_mp: int = Field(alias="addtionalMaxMp")
    additional_power: int = Field(alias="addtionalPower")
    additional_vitality: int = Field(alias="addtionalVitality")
    additional_agility: int = Field(alias="addtionalAgility")
    additional_weight: int = Field(alias="addionalWeight")  # sic
    additional_intelligence: int = Field(alias="addtionalIntelligence")
    additional_spirit: int = Field(alias="addtionalSpirit")
    additional_attack: int = Field(alias="addtionalAttack")
    additional_defense: int = Field(alias="addtionalDefense")
    additional_ability_defense: int = Field(alias="addtionalAbilityDefense")
    additional_ability_evasion_rate: int = Field(alias="addtionalAbilityEvasionRate")
    additional_magic: int = Field(alias="addtionalMagic")
    additional_luck: int = Field(alias="addtionalLuck")
    additional_accuracy_rate: int = Field(alias="addtionalAccuracyRate")
    additional_evasion_rate: int = Field(alias="addtionalEvasionRate")
    additional_ability_disturbed_rate: int = Field(
        alias="addtionalAbilityDisturbedRate"
    )
    additional_critical_rate: int = Field(alias="addtionalCriticalRate")
    additional_damage_dirmeter: int = Field(alias="addtionalDamageDirmeter")
    additional_ability_defense_rate: int = Field(alias="addtionalAbilityDefenseRate")
    additional_accuracy_count: int = Field(alias="addtionalAccuracyCount")
    additional_evasion_count: int = Field(alias="addtionalEvasionCount")
    additional_defense_count: int = Field(alias="addtionalDefenseCount")
    additional_magic_defense_count: int = Field(alias="addtionalMagicDefenseCount")
    current_condition_list: PrimitiveListWrapper[int] = Field(
        alias="currentConditionList"
    )

    @field_validator(
        "current_mp_count_list",
        "additional_max_mp_count_list",
        "current_condition_list",
        mode="before",
    )
    def deserialize_json(cls, v: str) -> JsonDict:
        return cast(JsonDict, json.loads(v))

    @field_serializer(
        "current_mp_count_list",
        "additional_max_mp_count_list",
        "current_condition_list",
    )
    def serialize_json(self, obj: BaseModel) -> str:
        return obj.model_dump_json()


class AbilityModel(BaseModel):
    ability_id: int = Field(alias="abilityId")
    content_id: int = Field(alias="contentId")
    skill_level: int = Field(alias="skillLevel")
    ability_name: str = Field(alias="abilityName")


class AbilitySlotModel(BaseModel):
    level: int
    slot_info: KeyValueList[int, str] = Field(alias="slotInfo")

    @field_validator("slot_info", mode="before")
    def deserialize_json(cls, v: str) -> JsonDict:
        return cast(JsonDict, json.loads(v))

    @field_serializer("slot_info")
    def serialize_json(self, obj: BaseModel) -> str:
        return obj.model_dump_json()


class JobModel(BaseModel):
    id: int
    level: int
    current_proficiency: int = Field(alias="currentProficiency")


class CharacterModel(BaseModel):
    id: int = Field(alias="id")
    character_status_id: int = Field(alias="characterStatusId")
    is_enable_corps: bool = Field(alias="isEnableCorps")
    job_id: int = Field(alias="jobId")
    name: str = Field(alias="name")
    current_exp: int = Field(alias="currentExp")
    parameter: CharacterParameterModel = Field(alias="parameter")
    command_list: PrimitiveListWrapper[int] = Field(alias="commandList")
    ability_list: ModelListWrapper[AbilityModel] = Field(alias="abilityList")
    ability_slot_data_list: ModelListWrapper[AbilitySlotModel] = Field(
        alias="abilitySlotDataList"
    )
    job_list: ModelListWrapper[JobModel] = Field(alias="jobList")
    equipment_list: str = Field(alias="equipmentList")
    addition_order_owned_ability_ids: PrimitiveListWrapper[int] = Field(
        alias="additionOrderOwnedAbilityIds"
    )
    sort_order_owned_ability_ids: str = Field(alias="sortOrderOwnedAbilityIds")
    ability_dictionary: str = Field(alias="abilityDictionary")
    skill_level_targets: str = Field(alias="skillLevelTargets")
    learning_abilities: str = Field(alias="learningAbilitys")
    equipment_abilities_: str = Field(alias="equipmentAbilitys")
    number_of_battles: int = Field(alias="numberOfButtles")
    owned_monster_id: int = Field(alias="ownedMonsterId")
    magic_stone_id: int = Field(alias="magicStoneId")
    magic_learning_value: int = Field(alias="magicLearningValue")
    is_default_name: bool = Field(alias="isDefaultName")

    @field_validator(
        "parameter",
        "command_list",
        "ability_list",
        "ability_slot_data_list",
        "job_list",
        "addition_order_owned_ability_ids",
        mode="before",
    )
    def deserialize_json(cls, v: str) -> JsonDict:
        return cast(JsonDict, json.loads(v))

    @field_serializer(
        "parameter",
        "command_list",
        "ability_list",
        "ability_slot_data_list",
        "job_list",
        "addition_order_owned_ability_ids",
    )
    def serialize_json(self, obj: BaseModel) -> str:
        return obj.model_dump_json()


class UserData(BaseModel):
    corps_list: str = Field(alias="corpsList")
    corps_slots: str = Field(alias="corpsSlots")
    owned_character_list: ModelListWrapper[CharacterModel] = Field(
        alias="ownedCharacterList"
    )
    released_jobs: PrimitiveListWrapper[int] = Field(alias="releasedJobs")
    owned_gil: int = Field(alias="owendGil")  # sic
    play_time: float = Field(alias="playTime")
    normal_owned_items: ModelListWrapper[ItemModel] = Field(alias="normalOwnedItemList")
    important_owned_items: ModelListWrapper[ItemModel] = Field(
        alias="importantOwendItemList"
    )
    normal_owned_item_sort_id_list: PrimitiveListWrapper[int] = Field(
        alias="normalOwnedItemSortIdList"
    )
    current_area: str = Field(alias="currentArea")
    current_location: str = Field(alias="currentLocation")
    owned_transportations: str = Field(alias="ownedTransportationList")
    owned_crystal_flags: PrimitiveListWrapper[bool] = Field(
        alias="owendCrystalFlags"
    )  # sic
    config_data: str = Field(alias="configData")
    warehouse_items: str = Field(alias="warehouseItemList")
    owned_key_items: str = Field(alias="ownedKeyWaordList")  # sic
    owned_magics: PrimitiveListWrapper[int] = Field(alias="ownedMagicList")
    learned_abilities: PrimitiveListWrapper[int] = Field(alias="learnedAbilityList")
    escape_count: int = Field(alias="escapeCount")
    battle_count: int = Field(alias="battleCount")
    corps_slot_index: int = Field(alias="corpsSlotIndex")
    open_chest_count: int = Field(alias="openChestCount")
    owned_magic_stones: PrimitiveListWrapper[int] = Field(
        alias="ownedMagicStoneList"
    )  # Espers?
    steps: int = Field(alias="steps")
    save_complete_count: int = Field(alias="saveCompleteCount")
    monsters_killed_count: int = Field(alias="monstersKilledCount")
    total_gil: int = Field(alias="totalGil")
    cheat_settings: JsonDict = Field(alias="cheatSettingsData")
    is_opened_game_booster_window: bool = Field(alias="isOpenedGameBoosterWindow")

    @field_validator(
        "normal_owned_items",
        "owned_character_list",
        "owned_magic_stones",
        "normal_owned_item_sort_id_list",
        "important_owned_items",
        "owned_crystal_flags",
        "owned_magics",
        "learned_abilities",
        "released_jobs",
        mode="before",
    )
    def deserialize_json(cls, v: str) -> JsonDict:
        return cast(JsonDict, json.loads(v))

    @field_serializer(
        "normal_owned_items",
        "owned_character_list",
        "owned_magic_stones",
        "released_jobs",
        "important_owned_items",
        "normal_owned_item_sort_id_list",
        "owned_crystal_flags",
        "owned_magics",
        "learned_abilities",
    )
    def serialize_json(self, obj: BaseModel) -> str:
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
