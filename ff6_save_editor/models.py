import json
from datetime import datetime
from enum import IntEnum
from typing import Any, Generic, TypeVar, cast

from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict, Field, field_serializer, field_validator

JsonDict = dict[str, Any]


class BaseModel(PydanticBaseModel):
    model_config = ConfigDict(extra="forbid")


M = TypeVar("M", bound=BaseModel)
T = TypeVar("T")
K = TypeVar("K")


class ModelListWrapper(BaseModel, Generic[M]):
    target: list[M]

    @field_validator("target", mode="before")
    def deserialize_data(cls, v: list[str]) -> list[JsonDict]:
        return [cast(JsonDict, json.loads(i)) for i in v]

    @field_serializer("target")
    def serialize_data(self, items: list[M]) -> list[str]:
        return [i.model_dump_json(by_alias=True) for i in items]


class PrimitiveListWrapper(BaseModel, Generic[T]):
    target: list[T]


class ModelKeyValueList(BaseModel, Generic[K, M]):
    keys: list[K]
    values: list[M]

    @field_validator("values", mode="before")
    def deserialize_data(cls, v: list[str]) -> list[JsonDict]:
        return [cast(JsonDict, json.loads(i)) for i in v]

    @field_serializer("values")
    def serialize_data(self, items: list[M]) -> list[str]:
        return [i.model_dump_json(by_alias=True) for i in items]


class PrimitiveKeyValueList(BaseModel, Generic[K, T]):
    keys: list[K]
    values: list[T]


class ItemId(IntEnum):
    Item1 = 2
    Item2 = 3
    Item3 = 4
    Item4 = 5
    Item5 = 6
    Item6 = 7
    Item7 = 8
    Item8 = 9
    Item9 = 10
    Item10 = 11
    Item11 = 12
    Item12 = 13
    Item13 = 14
    Item14 = 15
    Item15 = 16
    Item16 = 17
    Item17 = 18
    Item18 = 19
    Item19 = 20
    Item20 = 21
    Item21 = 22
    Item22 = 23
    Item23 = 24
    Item24 = 26
    Item25 = 27
    Item26 = 28
    Item27 = 29
    Item28 = 30
    Item29 = 31
    Item30 = 32
    Item31 = 33
    Item32 = 34
    Item33 = 35
    Item34 = 36
    Item35 = 37
    Item36 = 38
    Item37 = 39
    Item38 = 40
    Item39 = 45
    Item40 = 48
    Item41 = 50
    Item42 = 58
    Item43 = 93
    Item44 = 95
    Item45 = 98
    Item46 = 99
    Item47 = 100
    Item48 = 103
    Item49 = 104
    Item50 = 106
    Item51 = 107
    Item52 = 108
    Item53 = 109
    Item54 = 110
    Item55 = 112
    Item56 = 113
    Item57 = 114
    Zantetsuken = 119
    Lightbringer = 120
    Item60 = 122
    Item61 = 123
    Item62 = 125
    Item63 = 127
    Item64 = 130
    Item65 = 134
    Item66 = 135
    Kagenui = 136
    Item68 = 138
    Item69 = 140
    Item70 = 141
    Item71 = 142
    Item72 = 143
    Item73 = 145
    Item74 = 146
    Item75 = 147
    Item76 = 148
    Item77 = 150
    Item78 = 151
    Item79 = 152
    Item80 = 153
    Item81 = 154
    Item82 = 155
    Item83 = 157
    Item84 = 158
    Item85 = 161
    Item86 = 162
    Item87 = 163
    Item88 = 164
    Item89 = 165
    Item90 = 167
    Item91 = 168
    Item92 = 170
    Item93 = 171
    Item94 = 173
    Item95 = 175
    Item96 = 176
    Item97 = 178
    Item98 = 181
    Item99 = 182
    TigerFang = 183
    Item101 = 197
    Item102 = 198
    Item103 = 199
    Item104 = 200
    Item105 = 201
    Item106 = 203
    Item107 = 204
    AegisShield = 205
    Item109 = 206
    FlameShield = 207
    Item111 = 208
    Item112 = 209
    GenjiShield = 211
    CursedShield = 213
    Item115 = 215
    Item116 = 216
    Item117 = 218
    Item118 = 219
    Item119 = 220
    Item120 = 221
    Item121 = 222
    Item122 = 223
    Item123 = 224
    Item124 = 227
    Item125 = 229
    Item126 = 230
    Item127 = 231
    Item128 = 232
    Item129 = 233
    RoyalCrown = 234
    DiamondHelm = 235
    CrystalHelm = 237
    GenjiHelm = 240
    Item134 = 244
    Item135 = 245
    Item136 = 247
    Item137 = 248
    Item138 = 249
    Item139 = 250
    Item140 = 251
    Item141 = 252
    Item142 = 253
    Item143 = 255
    Item144 = 256
    Item145 = 258
    RedJacket = 259
    Item147 = 260
    Item148 = 261
    Item149 = 264
    Item150 = 265
    GenjiArmor = 266
    Item152 = 268
    Item153 = 272
    Item154 = 273
    Item155 = 274
    Item156 = 275
    Item157 = 276
    Item158 = 277
    Item159 = 278
    Item160 = 279
    Item161 = 280
    Item162 = 281
    Item163 = 282
    Item164 = 283
    HermesSandals = 285
    Item166 = 286
    Item167 = 287
    Item168 = 288
    Item169 = 289
    Item170 = 290
    Item171 = 291
    Item172 = 292
    Item173 = 294
    Item174 = 295
    Item175 = 296
    Item176 = 297
    Item177 = 298
    Item178 = 299
    HerosRing = 300
    Ribbon = 301
    Item181 = 302
    Item182 = 303
    Item183 = 304
    Celestriad = 305
    Item185 = 306
    Item186 = 307
    Item187 = 308
    HyperWrist = 309
    MastersScroll = 310
    Item190 = 311
    Item191 = 312
    Item192 = 313
    Item193 = 314
    Item194 = 315
    Item195 = 316
    Item196 = 318
    Item197 = 319
    Item198 = 320
    AlarmEarring = 324
    Item200 = 325
    Item201 = 326
    Item202 = 327
    Item203 = 328
    Item204 = 329


class ItemModel(BaseModel):
    content_id: ItemId = Field(alias="contentId")
    count: int


class CharacterParameterModel(BaseModel):
    current_hp: int = Field(alias="currentHP")
    current_mp: int = Field(alias="currentMP")
    current_mp_count_list: PrimitiveKeyValueList[int, int] = Field(
        alias="currentMpCountList"
    )
    additional_max_mp_count_list: PrimitiveKeyValueList[int, int] = Field(
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
        return obj.model_dump_json(by_alias=True)


class AbilityId(IntEnum):
    # Magic
    Cure = 31  # , content_id=361, skill_level=100, ability_name=""),)
    Cura = 32  # , content_id=362, skill_level=100, ability_name=""),)
    Curaga = 33  # , content_id=363, skill_level=100, ability_name=""),)
    Raise = 34  # , content_id=364, skill_level=100, ability_name=""),)
    Arise = 35  # , content_id=365, skill_level=100, ability_name=""),)
    Poisona = 36  # , content_id=366, skill_level=0, ability_name=""),)
    Esuna = 37  # , content_id=367, skill_level=100, ability_name=""),)
    Regen = 38  # , content_id=368, skill_level=100, ability_name=""),)
    Reraise = 39  # , content_id=369, skill_level=97, ability_name=""),)
    Fire = 40  # , content_id=370, skill_level=100, ability_name=""),)
    Blizzard = 41  # , content_id=371, skill_level=100, ability_name=""),)
    Thunder = 42  # , content_id=372, skill_level=100, ability_name=""),)
    Poison = 43  # , content_id=373, skill_level=0, ability_name=""),)
    Drain = 44  # , content_id=374, skill_level=100, ability_name=""),)
    Fira = 45  # , content_id=375, skill_level=100, ability_name=""),)
    Blizzara = 46  # , content_id=376, skill_level=100, ability_name=""),)
    Thundara = 47  # , content_id=377, skill_level=100, ability_name=""),)
    Bio = 48  # , content_id=378, skill_level=0, ability_name=""),)
    Firaga = 49  # , content_id=379, skill_level=100, ability_name=""),)
    Blizzaga = 50  # , content_id=380, skill_level=64, ability_name=""),)
    Thundaga = 51  # , content_id=381, skill_level=64, ability_name=""),)
    Break = 52  # , content_id=382, skill_level=0, ability_name=""),)
    Death = 53  # , content_id=383, skill_level=0, ability_name=""),)
    Holy = 54  # , content_id=384, skill_level=100, ability_name=""),)
    Flare = 55  # , content_id=385, skill_level=100, ability_name=""),)
    Gravity = 56  # , content_id=386, skill_level=0, ability_name=""),)
    Graviga = 57  # , content_id=387, skill_level=39, ability_name=""),)
    Banish = 58  # , content_id=388, skill_level=100, ability_name=""),)
    Meteor = 59  # , content_id=389, skill_level=0, ability_name=""),)
    Ultima = 60  # , content_id=390, skill_level=0, ability_name=""),)
    Quake = 61  # , content_id=391, skill_level=100, ability_name=""),)
    Tornado = 62  # , content_id=392, skill_level=39, ability_name=""),)
    Meltdown = 63  # , content_id=393, skill_level=0, ability_name=""),)
    Libra = 64  # , content_id=394, skill_level=0, ability_name=""),)
    Slow = 65  # , content_id=395, skill_level=0, ability_name=""),)
    Rasp = 66  # , content_id=396, skill_level=100, ability_name=""),)
    Silence = 67  # , content_id=397, skill_level=0, ability_name=""),)
    Protect = 68  # , content_id=398, skill_level=100, ability_name=""),)
    Sleep = 69  # , content_id=399, skill_level=0, ability_name=""),)
    Confuse = 70  # , content_id=400, skill_level=0, ability_name=""),)
    Haste = 71  # , content_id=401, skill_level=0, ability_name=""),)
    Stop = 72  # , content_id=402, skill_level=100, ability_name=""),)
    Berserk = 73  # , content_id=403, skill_level=0, ability_name=""),)
    Float = 74  # , content_id=404, skill_level=0, ability_name=""),)
    Imp = 75  # , content_id=405, skill_level=0, ability_name=""),)
    Reflect = 76  # , content_id=406, skill_level=0, ability_name=""),)
    Shell = 77  # , content_id=407, skill_level=100, ability_name=""),)
    Vanish = 78  # , content_id=408, skill_level=0, ability_name=""),)
    Hastega = 79  # , content_id=409, skill_level=0, ability_name=""),)
    Slowga = 80  # , content_id=410, skill_level=0, ability_name=""),)
    Osmose = 81  # , content_id=411, skill_level=100, ability_name=""),)
    Teleport = 82  # , content_id=412, skill_level=100, ability_name=""),)
    Quick = 83  # , content_id=413, skill_level=100, ability_name=""),)
    Dispel = 84  # , content_id=414, skill_level=100, ability_name=""),)

    # Bushido
    Fang = 124
    Sky = 125
    Tiger = 126
    Flurry = 127
    Dragon = 128
    Eclipse = 129
    Tempest = 130
    Oblivion = 131

    # Blitz
    RagingFist = 132
    AuraCannon = 133
    MeteorStrike = 134
    RisingPhoenix = 135
    Chakra = 136
    RazorGale = 137
    SoulSpiral = 138
    PhantomRush = 139

    # Lore
    Ability16 = 140
    Ability17 = 141
    Ability18 = 142
    AquaBreath = 143
    Ability20 = 144
    Ability21 = 145
    Ability22 = 146
    RevengeBlast = 147
    Ability24 = 148
    Ability25 = 149
    Ability26 = 150
    Ability27 = 151
    Ability28 = 152
    Ability29 = 153
    Ability30 = 154
    Ability31 = 155
    Ability32 = 156
    Ability33 = 157
    Transfusion = 158
    Ability35 = 159
    Stone = 160
    Ability37 = 161
    Ability38 = 162
    Ability39 = 163
    Ability40 = 164
    Ability41 = 165
    Ability42 = 166
    Ability43 = 167
    Ability44 = 168
    Ability45 = 169
    Ability46 = 170
    Ability47 = 171

    Ability48 = 201
    Ability49 = 210
    Ability50 = 211
    Ability51 = 212
    Ability52 = 213
    Ability53 = 214
    Ability54 = 215
    Ability55 = 216
    Ability56 = 218
    Ability57 = 219
    Ability58 = 220
    Ability59 = 221
    Ability60 = 222
    Ability61 = 223
    Ability62 = 224
    Ability63 = 225
    Ability64 = 228
    Ability65 = 229
    Ability66 = 230
    Ability67 = 231
    Ability68 = 232
    Ability69 = 233
    Ability70 = 234
    Ability71 = 235
    Ability72 = 236
    Ability73 = 237
    Ability74 = 238
    Ability75 = 239
    Ability76 = 253
    Ability77 = 259
    Ability78 = 292

    # Rage
    RageGuard = 800
    RageImperialSoldier = 801
    RageTemplar = 802
    RageNinja = 803
    RageSamurai = 804
    RageBorghese = 805
    RageMagnaRoaderPurple = 806
    RageYojimbo = 807
    RageCloud = 808
    RageMisty = 809
    RageAlJabr = 810
    RageZaghrem = 811
    RageApocrypha = 812
    RageDarkForce = 813
    RageAngelWhisper = 814
    RageOversoul = 815
    RageSkeletalHorror = 816
    RageCommander = 817
    RageMu = 818
    RageWererat = 819
    RageMugbear = 820
    RageBelmodar = 821
    RageMuudSuud = 822
    RageLeafBunny = 823
    RageStrayCat = 824
    RageSilverLobo = 825
    RageDoberman = 826
    RageMegalodoth = 827
    RageFidor = 828
    RageBriareus = 829
    RageSuriander = 830
    RageChimera = 831
    RageBehemoth = 832
    RageFafnir = 833
    RageLesserLopros = 834
    RageFossilDragon = 835
    RageHolyDragon = 836
    RageFiendDragon = 837
    RageBrachiosaur = 838
    RageTyrannosaur = 839
    RageDarkwind = 840
    RageAepyornis = 841
    RageVulture = 842
    RageVasegiatta = 843
    RageZokka = 844
    RageTrapper = 845
    RageHornet = 846
    RageNettlehopper = 847
    RageDeltaBeetle = 848
    RageKillerMantis = 849
    RageTrillium = 850
    RageRafflesia = 851
    RageTumbleweed = 852
    RageVampireThorn = 853
    RageCartagra = 854
    RageNautiloid = 855
    Rage0 = 856
    RageExocite = 857
    RageAnguiform = 858
    RageLeapFrog = 859
    RageLizard = 860
    RageLitworChicken = 861
    RageSlagworm = 862
    RageHellsRider = 863
    RageOnionKnight = 864
    Rage1 = 865
    RageMagitekArmor = 866
    RageSkyArmor = 867
    RageSatellite = 868
    RageArmoredWeapon = 869
    RageSpritzer = 870
    RageFlan = 871
    RageOutcast = 872
    RageHumpty = 873
    RageBrainpan = 874
    RageCruller = 875
    RageCactuar = 876
    RageBandit = 877
    RageHarvester = 878
    RageBomb = 879
    RageStillLife = 880
    RageLunatys = 881
    RageVeilDancer = 882
    RageHillGigas = 883
    RageTonberry = 884
    RageMagicUrn = 885
    RageMover = 886
    RageFigaroLizard = 887
    RageDevoahan = 888
    RageAspiran = 889
    RageGhost = 890
    RageCrawler = 891
    RageSandRay = 892
    RageAlacran = 893
    RageActinian = 894
    RageSandhorse = 895
    RageDarkside = 896
    RageMalboro = 897
    RageUrok = 898
    RageFoper = 899
    RageGuardLeader = 900
    RageCorporal = 901
    RageGeneral = 902
    RageCovert = 903
    RageKamui = 904
    RageWarlock = 905
    RageCherry = 906
    RageJoker = 907
    RageIronFist = 908
    RageDevil = 909
    RageProvoker = 910
    RageCloudwraith = 911
    RageMahadeva = 912
    RageVectorHound = 913
    RagePeeper = 914
    RageStunner = 915
    RageSorath = 916
    RageDestroyer = 917
    RageChippirabbit = 918
    RageCoeurlCat = 919
    RageBloodfang = 920
    RageHuntingHound = 921
    RageGorgias = 922
    RageDon = 923
    RageMurussu = 924
    RageWartpuck = 925
    RageGorgimera = 926
    RageBehemothKing = 927
    RageVectorLythos = 928
    RageWyvern = 929
    RageZombieDragon = 930
    RageDragon = 931
    RagePrimevalDragon = 932
    RageWeredragon = 933
    RageCirpius = 934
    RageSprinter = 935
    RageLenergia = 936
    RageMarchosias = 937
    RageGloomwind = 938
    RageDropper = 939
    RageRockWasp = 940
    RageGrasswyrm = 941
    RageLuridan = 942
    RageTwinscythe = 943
    RageParaladia = 944
    RageExoray = 945
    RageCrusher = 946
    RageOuroboros = 947
    RageAcrophies = 948
    RageSchmidt = 949
    RageDevourer = 950
    RageCancer = 951
    RageGigantoad = 952
    RageBasilisk = 953
    RageMedusaChicken = 954
    RageLandworm = 955
    RageTestRider = 956
    RagePlutoArmor = 957
    RageOnionDasher = 958
    RageHeavyArmor = 959
    RageChase = 960
    RageGamma = 961
    RagePoplium = 962
    RageIntanger = 963
    RageMisfit = 964
    RageCreature = 965
    RageEnuo = 966
    RageDeepeye = 967
    RageUnseelie = 968
    RageNeckHunter = 969
    RageGrenade = 970
    RageAlluringRider = 971
    RagePandora = 972
    RageBladeDancer = 973
    RageGigantos = 974
    RageMagnaRoaderRed = 975
    RageLycaon = 976
    RageParasite = 977
    RageMoonform = 978
    RageSpecter = 979
    RageGreatMalboro = 980
    RageBonnacon = 981
    RageOceanus = 982
    RageLivingDead = 983
    RageFace = 984
    RageOutsider = 985
    RageCoco = 986
    RageZeveak = 987
    RageNightwalker = 988
    RageDemonKnight = 989
    RageImperialElite = 990
    RageDesertHare = 991
    RageWizard = 992
    RageDevilFist = 993
    RageIlluyankas = 994
    RageSergeant = 995
    RageAspidochelon = 996
    RageKnotty = 997
    RageLunaWolf = 998
    RageBelzecue = 999
    RageCaladrius = 1000
    RageTzakmaqiel = 1001
    RageLukhavi = 1002
    RageEukaryote = 1003
    RageLandGrillon = 1004
    RageGoetia = 1005
    RageGreaterMantis = 1006
    RageBogy = 1007
    RagePurusa = 1008
    RageBlackDragon = 1009
    RageAdamankary = 1010
    RageDante = 1011
    RagePlatinumDragon = 1012
    RageDuelArmor = 1013
    RagePsycho = 1014
    RageMousse = 1015
    RageShamblingCorpse = 1016
    RagePunishe = 1017
    RageBalloon = 1018
    RageGobbledygook = 1019
    RageGreatBehemoth = 1020
    RageScorpion = 1021
    RageChaosDragon = 1022
    RageSpitfire = 1023
    RageVectorChimera = 1024
    RageLich = 1025
    RageRukh = 1026
    RageMagnaRoaderYellow = 1027
    RageBug = 1028
    RageSeaflower = 1029
    RageFortis = 1030
    RageVenobennu = 1031
    RageGalypdes = 1032
    RageJunk = 1033
    RageMandrake = 1034
    RageValero = 1035
    RageAmduscias = 1036
    RageNecromancer = 1037
    RageGlasyaLabolas = 1038
    RageMagnaRoaderBrown = 1039
    RageWildRat = 1040
    RageGoldBear = 1041
    RageInnoSent = 1042
    RageClymenus = 1043
    RageGarm = 1044
    RageDaedalus = 1045
    RageBaalzephon = 1046
    RageAhriman = 1047
    RageDeathMachine = 1048
    RageMetalHitman = 1049
    RageIo = 1050

    Ability327 = 1051
    Ability328 = 1052
    Ability329 = 1053
    Ability330 = 1054

    Ability331 = 1532


class AbilityType(IntEnum):
    Magic = 7
    Bushido = 12
    Blitz = 15
    Lore = 17
    Dance = 22
    Rage = 23
    Unknown = 26


class AbilityModel(BaseModel):
    ability_id: AbilityId = Field(alias="abilityId")
    content_id: int = Field(alias="contentId")
    skill_level: int = Field(alias="skillLevel")
    ability_name: str = Field(alias="abilityName")


class AbilitySlotModel(BaseModel):
    level: int
    slot_info: PrimitiveKeyValueList[int, str] = Field(alias="slotInfo")

    @field_validator("slot_info", mode="before")
    def deserialize_json(cls, v: str) -> JsonDict:
        return cast(JsonDict, json.loads(v))

    @field_serializer("slot_info")
    def serialize_json(self, obj: BaseModel) -> str:
        return obj.model_dump_json(by_alias=True)


class JobModel(BaseModel):
    id: int
    level: int
    current_proficiency: int = Field(alias="currentProficiency")


class CharacterId(IntEnum):
    Terra = 1
    Wedge = 2
    Biggs = 3
    Kefka = 4
    Locke = 5
    Moglin = 6
    Mogret = 7
    Moggie = 8
    Molulu = 9
    Moghan = 10
    Moguel = 11
    Mogsy = 12
    Mogwin = 13
    Mugmug = 14
    Cosmog = 15
    Mog = 16
    Edgar = 17
    Sabin = 18
    Shadow = 19
    Banon = 20
    MogNpc = 21  # The non-playable version of Mog
    Celes = 22
    Cyan = 23
    Mystery = 24  # Real name is '??????'
    Gau = 25
    Setzer = 26
    Maduin = 27
    Strago = 28
    Relm = 29
    Leo = 30
    Gestahl = 31
    Gogo = 32
    Umaro = 33


class CharacterModel(BaseModel):
    id: CharacterId = Field(alias="id")
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
    equipment_list: ModelKeyValueList[int, ItemModel] = Field(alias="equipmentList")
    addition_order_owned_ability_ids: PrimitiveListWrapper[int] = Field(
        alias="additionOrderOwnedAbilityIds"
    )
    sort_order_owned_ability_ids: str = Field(alias="sortOrderOwnedAbilityIds")
    ability_dictionary: ModelKeyValueList[
        AbilityType, ModelListWrapper[AbilityModel]
    ] = Field(alias="abilityDictionary")
    skill_level_targets: str = Field(alias="skillLevelTargets")
    learning_abilities: str = Field(alias="learningAbilitys")
    equipment_abilities: PrimitiveListWrapper[int] = Field(alias="equipmentAbilitys")
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
        "equipment_list",
        "ability_dictionary",
        "equipment_abilities",
        mode="before",
    )
    def deserialize_json(cls, v: str) -> JsonDict:
        return cast(JsonDict, json.loads(v))

    @field_serializer(
        "parameter",
        "command_list",
        "ability_dictionary",
        "ability_list",
        "ability_slot_data_list",
        "job_list",
        "addition_order_owned_ability_ids",
        "equipment_list",
        "equipment_abilities",
    )
    def serialize_json(self, obj: BaseModel) -> str:
        return obj.model_dump_json(by_alias=True)


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
        return obj.model_dump_json(by_alias=True)


class GlobalValuesKey(IntEnum):
    CursedShieldBattles = 9


class DataStorageModel(BaseModel):
    scenario: list[int]
    treasure: list[int]
    global_values: list[int] = Field(alias="global")
    area: list[int]
    map: list[int]
    selected: int
    item_selected: int = Field(alias="itemSelected")
    transportation: list[str]  # TODO: Validate type


class SaveModel(BaseModel):
    id: int
    picture_data: str = Field(alias="pictureData")
    user_data: UserData = Field(alias="userData")
    config_data: str = Field(alias="configData")
    data_storage: DataStorageModel = Field(alias="dataStorage")
    map_data: str = Field(alias="mapData")
    timestamp: datetime = Field(alias="timeStamp")
    play_time: float = Field(alias="playTime")
    clear_flag: int = Field(alias="clearFlag")
    is_complete_flag: int = Field(alias="isCompleteFlag")

    @field_validator(
        "user_data",
        "data_storage",
        mode="before",
    )
    def deserialize_data(cls, v: str) -> JsonDict:
        return cast(JsonDict, json.loads(v))

    @field_serializer(
        "user_data",
        "data_storage",
    )
    def serialize_data(self, user_data: UserData) -> str:
        return user_data.model_dump_json(by_alias=True)

    @field_validator("timestamp", mode="before")
    def deserialize_timestamp(cls, v: str) -> datetime:
        return datetime.strptime(v, "%m/%d/%Y %I:%M:%S %p")

    @field_serializer("timestamp")
    def serialize_timestamp(self, timestamp: datetime) -> str:
        return timestamp.strftime("%m/%d/%Y %I:%M:%S %p")
