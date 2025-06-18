import json
from datetime import datetime
from enum import IntEnum
from typing import Any, Generic, Literal, TypeVar, cast

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
        return [cast("JsonDict", json.loads(i)) for i in v]

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
        return [cast("JsonDict", json.loads(i)) for i in v]

    @field_serializer("values")
    def serialize_data(self, items: list[M]) -> list[str]:
        return [i.model_dump_json(by_alias=True) for i in items]


class PrimitiveKeyValueList(BaseModel, Generic[K, T]):
    keys: list[K]
    values: list[T]


class ItemId(IntEnum):
    Item0 = 0
    Item1 = 1
    Item2 = 2
    Item3 = 3
    Item4 = 4
    Item5 = 5
    Item6 = 6
    Item7 = 7
    Item8 = 8
    Item9 = 9
    Item10 = 10
    Item11 = 11
    Item12 = 12
    Item13 = 13
    Item14 = 14
    Item15 = 15
    Item16 = 16
    Item17 = 17
    Item18 = 18
    Item19 = 19
    Item20 = 20
    Item21 = 21
    Item22 = 22
    Item23 = 23
    Item24 = 24
    Item25 = 25
    Item26 = 26
    Item27 = 27
    Item28 = 28
    Item29 = 29
    Item30 = 30
    Item31 = 31
    Item32 = 32
    Item33 = 33
    Item34 = 34
    Item35 = 35
    Item36 = 36
    Item37 = 37
    Item38 = 38
    Item39 = 39
    Item40 = 40
    Item41 = 41
    Item42 = 42
    Item43 = 43
    Item44 = 44
    Item45 = 45
    Item46 = 46
    Item47 = 47
    Item48 = 48
    Item49 = 49
    Item50 = 50
    Item51 = 51
    Item52 = 52
    Item53 = 53
    Item54 = 54
    Item55 = 55
    Item56 = 56
    Item57 = 57
    Item58 = 58
    Item59 = 59
    Item60 = 60
    Item61 = 61
    Item62 = 62
    Item63 = 63
    Item64 = 64
    Item65 = 65
    Item66 = 66
    Item67 = 67
    Item68 = 68
    Item69 = 69
    Item70 = 70
    Item71 = 71
    Item72 = 72
    Item73 = 73
    Item74 = 74
    Item75 = 75
    Item76 = 76
    Item77 = 77
    Item78 = 78
    Item79 = 79
    Item80 = 80
    Item81 = 81
    Item82 = 82
    Item83 = 83
    Item84 = 84
    Item85 = 85
    Item86 = 86
    Item87 = 87
    Item88 = 88
    Item89 = 89
    Item90 = 90
    Item91 = 91
    Item92 = 92
    Item93 = 93
    Item94 = 94
    Item95 = 95
    Item96 = 96
    Item97 = 97
    Item98 = 98
    Item99 = 99
    Item100 = 100
    Item101 = 101
    Item102 = 102
    Item103 = 103
    Item104 = 104
    Item105 = 105
    Item106 = 106
    Item107 = 107
    Item108 = 108
    Item109 = 109
    Item110 = 110
    Item111 = 111
    Item112 = 112
    Item113 = 113
    Item114 = 114
    Item115 = 115
    Item116 = 116
    Item117 = 117
    Item118 = 118
    Zantetsuken = 119
    Lightbringer = 120
    Item121 = 121
    Item122 = 122
    Item123 = 123
    Item124 = 124
    Item125 = 125
    Item126 = 126
    Item127 = 127
    Item128 = 128
    Item129 = 129
    Item130 = 130
    Item131 = 131
    Item132 = 132
    Item133 = 133
    Item134 = 134
    Item135 = 135
    Kagenui = 136
    Item137 = 137
    Item138 = 138
    Item139 = 139
    Item140 = 140
    Item141 = 141
    Item142 = 142
    Item143 = 143
    Item144 = 144
    Item145 = 145
    Item146 = 146
    Item147 = 147
    Item148 = 148
    Item149 = 149
    Item150 = 150
    Item151 = 151
    Item152 = 152
    Item153 = 153
    Item154 = 154
    Item155 = 155
    Item156 = 156
    Item157 = 157
    Item158 = 158
    Item159 = 159
    Item160 = 160
    Item161 = 161
    Item162 = 162
    Item163 = 163
    Item164 = 164
    Item165 = 165
    Item166 = 166
    Item167 = 167
    Item168 = 168
    Item169 = 169
    Item170 = 170
    Item171 = 171
    Item172 = 172
    Item173 = 173
    Item174 = 174
    Item175 = 175
    Item176 = 176
    Item177 = 177
    Item178 = 178
    Item179 = 179
    Item180 = 180
    Item181 = 181
    Item182 = 182
    TigerFang = 183
    Item184 = 184
    Item185 = 185
    Item186 = 186
    Item187 = 187
    Item188 = 188
    Item189 = 189
    Item190 = 190
    Item191 = 191
    Item192 = 192
    Item193 = 193
    Item194 = 194
    Item195 = 195
    Item196 = 196
    Item197 = 197
    Item198 = 198
    Item199 = 199
    Item200 = 200
    Item201 = 201
    Item202 = 202
    Item203 = 203
    Item204 = 204
    AegisShield = 205
    Item206 = 206
    FlameShield = 207
    Item208 = 208
    Item209 = 209
    Item210 = 210
    GenjiShield = 211
    Item212 = 212
    CursedShield = 213
    Item214 = 214
    Item215 = 215
    Item216 = 216
    Item217 = 217
    Item218 = 218
    Item219 = 219
    Item220 = 220
    Item221 = 221
    Item222 = 222
    Item223 = 223
    Item224 = 224
    Item225 = 225
    Item226 = 226
    Item227 = 227
    Item228 = 228
    Item229 = 229
    Item230 = 230
    Item231 = 231
    Item232 = 232
    Item233 = 233
    RoyalCrown = 234
    DiamondHelm = 235
    Item236 = 236
    CrystalHelm = 237
    Item238 = 238
    Item239 = 239
    GenjiHelm = 240
    Item241 = 241
    Item242 = 242
    Item243 = 243
    Item244 = 244
    Item245 = 245
    Item246 = 246
    Item247 = 247
    Item248 = 248
    Item249 = 249
    Item250 = 250
    Item251 = 251
    Item252 = 252
    Item253 = 253
    Item254 = 254
    Item255 = 255
    Item256 = 256
    Item257 = 257
    Item258 = 258
    RedJacket = 259
    Item260 = 260
    Item261 = 261
    Item262 = 262
    Item263 = 263
    Item264 = 264
    Item265 = 265
    GenjiArmor = 266
    Item267 = 267
    Item268 = 268
    Item269 = 269
    Item270 = 270
    Item271 = 271
    Item272 = 272
    Item273 = 273
    Item274 = 274
    Item275 = 275
    Item276 = 276
    Item277 = 277
    Item278 = 278
    Item279 = 279
    Item280 = 280
    Item281 = 281
    Item282 = 282
    Item283 = 283
    Item284 = 284
    HermesSandals = 285
    Item286 = 286
    Item287 = 287
    Item288 = 288
    Item289 = 289
    Item290 = 290
    Item291 = 291
    Item292 = 292
    Item293 = 293
    Item294 = 294
    Item295 = 295
    Item296 = 296
    Item297 = 297
    Item298 = 298
    Item299 = 299
    HerosRing = 300
    Ribbon = 301
    Item302 = 302
    Item303 = 303
    Item304 = 304
    Celestriad = 305
    Item306 = 306
    Item307 = 307
    Item308 = 308
    HyperWrist = 309
    MastersScroll = 310
    Item311 = 311
    Item312 = 312
    Item313 = 313
    Item314 = 314
    Item315 = 315
    Item316 = 316
    Item317 = 317
    Item318 = 318
    Item319 = 319
    Item320 = 320
    Item321 = 321
    Item322 = 322
    Item323 = 323
    AlarmEarring = 324
    Item325 = 325
    Item326 = 326
    Item327 = 327
    Item328 = 328
    Item329 = 329
    Item330 = 330
    Item331 = 331
    Item332 = 332
    Item333 = 333
    Item334 = 334
    Item335 = 335
    Item336 = 336
    Item337 = 337
    Item338 = 338
    Item339 = 339
    Item340 = 340
    Item341 = 341
    Item342 = 342
    Item343 = 343
    Item344 = 344
    Item345 = 345
    Item346 = 346
    Item347 = 347
    Item348 = 348
    Item349 = 349


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
        return cast("JsonDict", json.loads(v))

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


class EsperId(IntEnum):
    Ramuh = 62
    Kirin = 63
    Siren = 64
    CaitSith = 65
    Ifrit = 66
    Shiva = 67
    Unicorn = 68
    Maduin = 69
    Catoblepas = 70
    Phantom = 71
    Carbuncle = 72
    Bismarck = 73
    Golem = 74
    ZonaSeeker = 75
    Seraph = 76
    Quetzalli = 77
    Fenrir = 78
    Valigarmanda = 79
    Midgarsormr = 80
    Lakshmi = 81
    Alexander = 82
    Phoenix = 83
    Odin = 84
    Bahamut = 85
    Ragnarok = 86
    Crusader = 87
    Raiden = 88


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
        return cast("JsonDict", json.loads(v))

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
    sort_order_owned_ability_ids: PrimitiveListWrapper[int] = Field(
        alias="sortOrderOwnedAbilityIds"
    )
    ability_dictionary: ModelKeyValueList[
        AbilityType, ModelListWrapper[AbilityModel]
    ] = Field(alias="abilityDictionary")
    skill_level_targets: PrimitiveKeyValueList[int, str] = Field(
        alias="skillLevelTargets"
    )
    learning_abilities: PrimitiveListWrapper[int] = Field(alias="learningAbilitys")
    equipment_abilities: PrimitiveListWrapper[int] = Field(alias="equipmentAbilitys")
    number_of_battles: int = Field(alias="numberOfButtles")
    owned_monster_id: int = Field(alias="ownedMonsterId")
    esper_id: EsperId | Literal[0] = Field(alias="magicStoneId")
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
        "skill_level_targets",
        "learning_abilities",
        "sort_order_owned_ability_ids",
        mode="before",
    )
    def deserialize_json(cls, v: str) -> JsonDict:
        return cast("JsonDict", json.loads(v))

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
        "skill_level_targets",
        "learning_abilities",
        "sort_order_owned_ability_ids",
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
    owned_espers: PrimitiveListWrapper[EsperId] = Field(alias="ownedMagicStoneList")
    steps: int = Field(alias="steps")
    save_complete_count: int = Field(alias="saveCompleteCount")
    monsters_killed_count: int = Field(alias="monstersKilledCount")
    total_gil: int = Field(alias="totalGil")
    cheat_settings: JsonDict = Field(alias="cheatSettingsData")
    is_opened_game_booster_window: bool = Field(alias="isOpenedGameBoosterWindow")

    @field_validator(
        "normal_owned_items",
        "owned_character_list",
        "owned_espers",
        "normal_owned_item_sort_id_list",
        "important_owned_items",
        "owned_crystal_flags",
        "owned_magics",
        "learned_abilities",
        "released_jobs",
        mode="before",
    )
    def deserialize_json(cls, v: str) -> JsonDict:
        return cast("JsonDict", json.loads(v))

    @field_serializer(
        "normal_owned_items",
        "owned_character_list",
        "owned_espers",
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
        return cast("JsonDict", json.loads(v))

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
