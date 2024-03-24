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


class CountList(BaseModel, Generic[K, V]):
    keys: list[K]
    values: list[V]


class CharacterParameterModel(BaseModel):
    current_hp: int = Field(alias="currentHP")
    current_mp: int = Field(alias="currentMP")
    current_mp_count_list: CountList[int, int] = Field(alias="currentMpCountList")
    addtional_max_mp_count_list: CountList[int, int] = Field(
        alias="addtionalMaxMpCountList"
    )
    addtional_level: int = Field(alias="addtionalLevel")
    addtional_max_hp: int = Field(alias="addtionalMaxHp")
    addtional_max_mp: int = Field(alias="addtionalMaxMp")
    addtional_power: int = Field(alias="addtionalPower")
    addtional_vitality: int = Field(alias="addtionalVitality")
    addtional_agility: int = Field(alias="addtionalAgility")
    additonal_weight: int = Field(alias="addionalWeight")  # sic
    addtional_intelligence: int = Field(alias="addtionalIntelligence")
    addtional_spirit: int = Field(alias="addtionalSpirit")
    addtional_attack: int = Field(alias="addtionalAttack")
    addtional_defense: int = Field(alias="addtionalDefense")
    addtional_ability_defense: int = Field(alias="addtionalAbilityDefense")
    addtional_ability_evasion_rate: int = Field(alias="addtionalAbilityEvasionRate")
    addtional_magic: int = Field(alias="addtionalMagic")
    addtional_luck: int = Field(alias="addtionalLuck")
    addtional_accuracy_rate: int = Field(alias="addtionalAccuracyRate")
    addtional_evasion_rate: int = Field(alias="addtionalEvasionRate")
    addtional_ability_disturbed_rate: int = Field(alias="addtionalAbilityDisturbedRate")
    addtional_critical_rate: int = Field(alias="addtionalCriticalRate")
    addtional_damage_dirmeter: int = Field(alias="addtionalDamageDirmeter")
    addtional_ability_defense_rate: int = Field(alias="addtionalAbilityDefenseRate")
    addtional_accuracy_count: int = Field(alias="addtionalAccuracyCount")
    addtional_evasion_count: int = Field(alias="addtionalEvasionCount")
    addtional_defense_count: int = Field(alias="addtionalDefenseCount")
    addtional_magic_defense_count: int = Field(alias="addtionalMagicDefenseCount")
    current_condition_list: PrimitiveListWrapper[int] = Field(
        alias="currentConditionList"
    )

    @field_validator(
        "current_mp_count_list",
        "addtional_max_mp_count_list",
        "current_condition_list",
        mode="before",
    )
    def deserialize_json(cls, v: str) -> JsonDict:
        return cast(JsonDict, json.loads(v))

    @field_serializer(
        "current_mp_count_list", "addtional_max_mp_count_list", "current_condition_list"
    )
    def serialize_json(self, obj: BaseModel) -> str:
        return obj.model_dump_json()


class CharacterModel(BaseModel):
    id: int = Field(alias="id")
    character_status_id: int = Field(alias="characterStatusId")
    is_enable_corps: bool = Field(alias="isEnableCorps")
    job_id: int = Field(alias="jobId")
    name: str = Field(alias="name")
    current_exp: int = Field(alias="currentExp")
    parameter: CharacterParameterModel = Field(alias="parameter")
    command_list: str = Field(alias="commandList")
    ability_list: str = Field(alias="abilityList")
    ability_slot_data_list: str = Field(alias="abilitySlotDataList")
    job_list: str = Field(alias="jobList")
    equipment_list: str = Field(alias="equipmentList")
    addition_order_owned_ability_ids: str = Field(alias="additionOrderOwnedAbilityIds")
    sort_order_owned_ability_ids: str = Field(alias="sortOrderOwnedAbilityIds")
    ability_dictionary: str = Field(alias="abilityDictionary")
    skill_level_targets: str = Field(alias="skillLevelTargets")
    learning_abilities: str = Field(alias="learningAbilitys")
    equipment_abilities_: str = Field(alias="equipmentAbilitys")
    number_of_buttles: int = Field(alias="numberOfButtles")
    owned_monster_id: int = Field(alias="ownedMonsterId")
    magic_stone_id: int = Field(alias="magicStoneId")
    magic_learning_value: int = Field(alias="magicLearningValue")
    is_default_name: bool = Field(alias="isDefaultName")

    @field_validator("parameter", mode="before")
    def deserialize_json(cls, v: str) -> JsonDict:
        return cast(JsonDict, json.loads(v))

    @field_serializer("parameter")
    def serialize_json(self, obj: BaseModel) -> str:
        return obj.model_dump_json()


class UserData(BaseModel):
    corps_list: str = Field(alias="corpsList")
    corps_slots: str = Field(alias="corpsSlots")
    owned_character_list: ModelListWrapper[CharacterModel] = Field(
        alias="ownedCharacterList"
    )
    released_jobs: str = Field(alias="releasedJobs")
    owned_gil: int = Field(alias="owendGil")  # sic
    play_time: float = Field(alias="playTime")
    normal_owned_items: ModelListWrapper[ItemModel] = Field(alias="normalOwnedItemList")
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
    def deserialize_json(cls, v: str) -> JsonDict:
        return cast(JsonDict, json.loads(v))

    @field_serializer("normal_owned_items", "owned_character_list")
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
