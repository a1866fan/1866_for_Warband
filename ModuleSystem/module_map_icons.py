# -*- coding: UTF-8 -*-
####################################################################################################################
# Generated by Warband Module Decompiler
# All rights of the module belong to their respective owners
####################################################################################################################

from header_map_icons import *
from module_constants import *
from header_operations import *
from header_triggers import *
from ID_sounds import *

####################################################################################################################
#  Each map icon record contains the following fields:
#  1) Map icon id: used for referencing map icons in other files.
#     The prefix icon_ is automatically added before each map icon id.
#  2) Map icon flags. See header_map icons.py for a list of available flags
#  3) Mesh name.
#  4) Scale. 
#  5) Sound.
#  6) Offset x position for the flag icon.
#  7) Offset y position for the flag icon.
#  8) Offset z position for the flag icon.
####################################################################################################################

map_icons = [
  ("player", 0, "icon_outlaw_walker", 0.15, snd_footstep_grass, 0.15, 0.173, 0),
  ("player_horseman", 0, "icon_outlaw_soldier", 0.15, snd_gallop, 0.15, 0.173, 0),
  ("peasant", 0, "peasant_a", 0.15, snd_footstep_grass, 0.15, 0.173, 0),
  ("axeman", 0, "icon_bandit_walker", 0.15, snd_footstep_grass, 0.15, 0.173, 0),
  ("woman", 0, "woman_a", 0.15, snd_footstep_grass, 0.15, 0.173, 0),
  ("woman_b", 0, "woman_b", 0.15, snd_footstep_grass, 0.15, 0.173, 0),
  ("town", mcn_no_shadow, "map_town_a", 0.35, 0, 0, 0, 0),
  ("town_steppe", mcn_no_shadow, "map_town_steppe_a", 0.35, 0, 0, 0, 0),
  ("village_a", mcn_no_shadow, "map_village_a", 0.45, 0, 0, 0, 0),
  ("village_burnt_a", mcn_no_shadow, "map_village_burnt_a", 0.45, 0, 0, 0, 0),
  ("village_deserted_a", mcn_no_shadow, "map_village_deserted_a", 0.45, 0, 0, 0, 0),
  ("usa_soldier", 0, "icon_usa_soldier", 0.15, snd_gallop, 0.15, 0.173, 0),
  ("mexico_soldier", 0, "icon_mexico_soldier", 0.15, snd_gallop, 0.15, 0.173, 0),
  ("apache_soldier", 0, "icon_apache_soldier", 0.15, snd_gallop, 0.15, 0.173, 0),
  ("comanche_soldier", 0, "icon_comanche_soldier", 0.15, snd_gallop, 0.15, 0.173, 0),
  ("bandit_soldier", 0, "icon_bandit_soldier", 0.15, snd_gallop, 0.15, 0.173, 0),
  ("lawman_soldier", 0, "icon_lawman_soldier", 0.15, snd_gallop, 0.15, 0.173, 0),
  ("outlaw_soldier", 0, "icon_outlaw_soldier", 0.15, snd_gallop, 0.15, 0.173, 0),
  ("bounty_hunter", 0, "icon_bandit_walker", 0.15, snd_footstep_grass, 0.15, 0.173, 0),
  ("usa_town_a", mcn_no_shadow, "icon_usa_town_a", 0.5, 0, 0, 0, 0),
  ("usa_town_b", mcn_no_shadow, "icon_usa_town_b", 0.5, 0, 0, 0, 0),
  ("usa_town_hotel", mcn_no_shadow, "icon_usa_town_hotel", 0.2, 0, 0, 0, 0),
  ("usa_town_bank", mcn_no_shadow, "icon_usa_town_bank", 0.2, 0, 0, 0, 0),
  ("usa_village", mcn_no_shadow, "icon_usa_village", 0.5, 0, 0, 0, 0),
  ("usa_village_hotel", mcn_no_shadow, "icon_usa_village_hotel", 0.5, 0, 0, 0, 0),
  ("mexican_village", mcn_no_shadow, "icon_mexican_village", 0.6, 0, 0, 0, 0),
  ("mexican_village_hotel", mcn_no_shadow, "icon_mexican_town_hotel", 0.4, 0, 0, 0, 0),
  ("mexican_town_a", mcn_no_shadow, "icon_mexican_town_a", 0.5, 0, 0, 0, 0),
  ("mexican_town_hotel", mcn_no_shadow, "icon_mexican_town_hotel", 0.2, 0, 0, 0, 0),
  ("mexican_town_bank", mcn_no_shadow, "icon_mexican_town_bank", 0.2, 0, 0, 0, 0),
  ("bridge_a", mcn_no_shadow, "icon_bridge_a", 0.5, 0, 0, 0, 0),
  ("bridge_b", mcn_no_shadow, "icon_bridge_b", 0.5, 0, 0, 0, 0),
  ("bridge_c", mcn_no_shadow, "icon_bridge_c", 0.5, 0, 0, 0, 0),
  ("teepee_town", mcn_no_shadow, "icon_teepee_town", 0.5, 0, 0, 0, 0),
  ("teepee", mcn_no_shadow, "icon_teepee", 0.5, 0, 0, 0, 0),
  ("mine_small", mcn_no_shadow, "icon_mine_small", 1, 0, 0, 0, 0),
  ("mine_large", mcn_no_shadow, "icon_mine_large", 0.5, 0, 0, 0, 0),
  ("fort", mcn_no_shadow, "icon_fort", 0.3, 0, 0, 0, 0),
  ("cabin", mcn_no_shadow, "icon_cabin", 0.5, 0, 0, 0, 0),
  ("telegraph", mcn_no_shadow, "icon_telegraph", 0.6, 0, 0, 0, 0),
  ("graveyard", mcn_no_shadow, "icon_graveyard", 0.6, 0, 0, 0, 0),
  ("target", mcn_no_shadow, "target", 0.6, 0, 0, 0, 0),
  ("camp", mcn_no_shadow, "camp_tent", 0.13, 0, 0, 0, 0),
  ("ship", mcn_no_shadow, "icon_steamboat", 0.23, snd_footstep_grass, 0, 0.05, 0),
  ("ship_on_land", mcn_no_shadow, "icon_steamboat", 0.23, 0, 0, 0, 0),
  ("castle_a", mcn_no_shadow, "map_castle_a", 0.35, 0, 0, 0, 0),
  ("castle_b", mcn_no_shadow, "map_castle_b", 0.35, 0, 0, 0, 0),
  ("castle_c", mcn_no_shadow, "map_castle_c", 0.35, 0, 0, 0, 0),
  ("castle_d", mcn_no_shadow, "map_castle_d", 0.35, 0, 0, 0, 0),
  ("town_snow", mcn_no_shadow, "map_town_snow_a", 0.35, 0, 0, 0, 0),
  ("village_snow_a", mcn_no_shadow, "map_village_snow_a", 0.45, 0, 0, 0, 0),
  ("village_snow_burnt_a", mcn_no_shadow, "map_village_snow_burnt_a", 0.45, 0, 0, 0, 0),
  ("village_snow_deserted_a", mcn_no_shadow, "map_village_snow_deserted_a", 0.45, 0, 0, 0, 0),
  ("castle_snow_a", mcn_no_shadow, "map_castle_snow_a", 0.35, 0, 0, 0, 0),
  ("castle_snow_b", mcn_no_shadow, "map_castle_snow_b", 0.35, 0, 0, 0, 0),
  ("mule", 0, "icon_mule", 0.2, snd_footstep_grass, 0.15, 0.173, 0),
  ("cattle", 0, "icon_cow", 0.2, snd_footstep_grass, 0.15, 0.173, 0),
  ("steamboat", 0, "icon_steamboat", 0.2, 0, 0, 0, 0),
  ("deer", 0, "deer", 0.2, snd_gallop, 0.15, 0.173, 0),
  ("buffalo", 0, "icon_buffalo", 0.2, snd_footstep_horse, 0.15, 0.173, 0),
  ("horses", 0, "icon_horse_wild", 0.2, snd_gallop, 0.15, 0.173, 0),
  ("stagecoach", 0, "icon_stagecoach", 0.15, snd_footstep_grass, 0.15, 0.173, 0),
  ("wagon", 0, "icon_wagon", 0.15, snd_footstep_grass, 0.15, 0.173, 0),
  ("ambush", mcn_no_shadow, "icon_ambush", 1, 0, 0, 0, 0),
  ("training_ground", mcn_no_shadow, "training", 0.35, 0, 0, 0, 0),
  ("bridge_a", mcn_no_shadow, "map_river_bridge_a", 1.27, 0, 0, 0, 0),
  ("bridge_b", mcn_no_shadow, "map_river_bridge_b", 0.7, 0, 0, 0, 0),
  ("bridge_snow_a", mcn_no_shadow, "map_river_bridge_snow_a", 1.27, 0, 0, 0, 0),
  ("custom_banner_01", 0, "custom_map_banner_01", 0.3, 0, 0, 0, 0,
  [
    (ti_on_init_map_icon,[
      (store_trigger_param_1, ":var0"),
      (party_get_slot, ":var1", ":var0", 7),
      (try_begin),
        (ge, ":var1", 0),
        (cur_map_icon_set_tableau_material, "tableau_custom_banner_square", ":var1"),
      (try_end),
    ]),
  ]),
  ("custom_banner_02", 0, "custom_map_banner_02", 0.3, 0, 0, 0, 0,
  [
    (ti_on_init_map_icon,[
      (store_trigger_param_1, ":var0"),
      (party_get_slot, ":var1", ":var0", 7),
      (try_begin),
        (ge, ":var1", 0),
        (cur_map_icon_set_tableau_material, "tableau_custom_banner_short", ":var1"),
      (try_end),
    ]),
  ]),
  ("custom_banner_03", 0, "custom_map_banner_03", 0.3, 0, 0, 0, 0,
  [
    (ti_on_init_map_icon,[
      (store_trigger_param_1, ":var0"),
      (party_get_slot, ":var1", ":var0", 7),
      (try_begin),
        (ge, ":var1", 0),
        (cur_map_icon_set_tableau_material, "tableau_custom_banner_tall", ":var1"),
      (try_end),
    ]),
  ]),
  ("banner_01", 0, "map_flag_01", 0.3, 0, 0, 0, 0),
  ("banner_02", 0, "map_flag_04", 0.3, 0, 0, 0, 0),
  ("banner_03", 0, "map_flag_05", 0.3, 0, 0, 0, 0),
  ("banner_04", 0, "map_flag_03", 0.3, 0, 0, 0, 0),
  ("banner_05", 0, "map_flag_02", 0.3, 0, 0, 0, 0),
  ("banner_06", 0, "map_flag_06", 0.3, 0, 0, 0, 0),
  ("banner_07", 0, "map_flag_07", 0.3, 0, 0, 0, 0),
  ("banner_08", 0, "map_flag_08", 0.3, 0, 0, 0, 0),
  ("banner_09", 0, "map_flag_09", 0.3, 0, 0, 0, 0),
  ("banner_10", 0, "map_flag_10", 0.3, 0, 0, 0, 0),
  ("banner_11", 0, "map_flag_11", 0.3, 0, 0, 0, 0),
  ("banner_12", 0, "map_flag_12", 0.3, 0, 0, 0, 0),
  ("banner_13", 0, "map_flag_13", 0.3, 0, 0, 0, 0),
  ("banner_14", 0, "map_flag_14", 0.3, 0, 0, 0, 0),
  ("banner_15", 0, "map_flag_15", 0.3, 0, 0, 0, 0),
  ("banner_16", 0, "map_flag_36", 0.3, 0, 0, 0, 0),
  ("banner_17", 0, "map_flag_37", 0.3, 0, 0, 0, 0),
  ("banner_18", 0, "map_flag_38", 0.3, 0, 0, 0, 0),
  ("banner_19", 0, "map_flag_39", 0.3, 0, 0, 0, 0),
  ("banner_20", 0, "map_flag_40", 0.3, 0, 0, 0, 0),
  ("banner_21", 0, "map_flag_41", 0.3, 0, 0, 0, 0),
  ("banner_22", 0, "map_flag_42", 0.3, 0, 0, 0, 0),
  ("banner_23", 0, "map_flag_43", 0.3, 0, 0, 0, 0),
  ("banner_24", 0, "map_flag_44", 0.3, 0, 0, 0, 0),
  ("banner_25", 0, "map_flag_45", 0.3, 0, 0, 0, 0),
  ("banner_26", 0, "map_flag_d01", 0.3, 0, 0, 0, 0),
  ("banner_27", 0, "map_flag_46", 0.3, 0, 0, 0, 0),
  ("banner_28", 0, "map_flag_47", 0.3, 0, 0, 0, 0),
  ("banner_29", 0, "map_flag_48", 0.3, 0, 0, 0, 0),
  ("banner_30", 0, "map_flag_49", 0.3, 0, 0, 0, 0),
  ("banner_31", 0, "map_flag_50", 0.3, 0, 0, 0, 0),
  ("banner_32", 0, "map_flag_51", 0.3, 0, 0, 0, 0),
  ("banner_33", 0, "map_flag_52", 0.3, 0, 0, 0, 0),
  ("banner_34", 0, "map_flag_53", 0.3, 0, 0, 0, 0),
  ("banner_35", 0, "map_flag_54", 0.3, 0, 0, 0, 0),
  ("banner_36", 0, "map_flag_55", 0.3, 0, 0, 0, 0),
  ("banner_37", 0, "map_flag_56", 0.3, 0, 0, 0, 0),
  ("banner_38", 0, "map_flag_26", 0.3, 0, 0, 0, 0),
  ("banner_39", 0, "map_flag_27", 0.3, 0, 0, 0, 0),
  ("banner_40", 0, "map_flag_28", 0.3, 0, 0, 0, 0),
  ("banner_41", 0, "map_flag_29", 0.3, 0, 0, 0, 0),
  ("banner_42", 0, "map_flag_30", 0.3, 0, 0, 0, 0),
  ("banner_43", 0, "map_flag_31", 0.3, 0, 0, 0, 0),
  ("banner_44", 0, "map_flag_32", 0.3, 0, 0, 0, 0),
  ("banner_45", 0, "map_flag_33", 0.3, 0, 0, 0, 0),
  ("banner_46", 0, "map_flag_34", 0.3, 0, 0, 0, 0),
  ("banner_47", 0, "map_flag_35", 0.3, 0, 0, 0, 0),
  ("banner_48", 0, "map_flag_60", 0.3, 0, 0, 0, 0),
  ("banner_49", 0, "map_flag_d12", 0.3, 0, 0, 0, 0),
  ("banner_50", 0, "map_flag_d13", 0.3, 0, 0, 0, 0),
  ("banner_51", 0, "map_flag_d14", 0.3, 0, 0, 0, 0),
  ("banner_52", 0, "map_flag_d15", 0.3, 0, 0, 0, 0),
  ("banner_53", 0, "map_flag_d16", 0.3, 0, 0, 0, 0),
  ("banner_54", 0, "map_flag_d17", 0.3, 0, 0, 0, 0),
  ("banner_55", 0, "map_flag_d18", 0.3, 0, 0, 0, 0),
  ("banner_56", 0, "map_flag_d19", 0.3, 0, 0, 0, 0),
  ("banner_57", 0, "map_flag_d20", 0.3, 0, 0, 0, 0),
  ("banner_58", 0, "map_flag_d21", 0.3, 0, 0, 0, 0),
  ("banner_59", 0, "map_flag_e01", 0.3, 0, 0, 0, 0),
  ("banner_60", 0, "map_flag_e02", 0.3, 0, 0, 0, 0),
  ("banner_61", 0, "map_flag_e03", 0.3, 0, 0, 0, 0),
  ("banner_62", 0, "map_flag_e04", 0.3, 0, 0, 0, 0),
  ("banner_63", 0, "map_flag_e05", 0.3, 0, 0, 0, 0),
  ("banner_64", 0, "map_flag_e06", 0.3, 0, 0, 0, 0),
  ("banner_65", 0, "map_flag_e07", 0.3, 0, 0, 0, 0),
  ("banner_66", 0, "map_flag_e08", 0.3, 0, 0, 0, 0),
  ("banner_67", 0, "map_flag_e09", 0.3, 0, 0, 0, 0),
  ("banner_68", 0, "map_flag_e10", 0.3, 0, 0, 0, 0),
  ("banner_69", 0, "map_flag_e11", 0.3, 0, 0, 0, 0),
  ("banner_70", 0, "map_flag_16", 0.3, 0, 0, 0, 0),
  ("banner_71", 0, "map_flag_17", 0.3, 0, 0, 0, 0),
  ("banner_72", 0, "map_flag_18", 0.3, 0, 0, 0, 0),
  ("banner_73", 0, "map_flag_19", 0.3, 0, 0, 0, 0),
  ("banner_74", 0, "map_flag_23", 0.3, 0, 0, 0, 0),
  ("banner_75", 0, "map_flag_21", 0.3, 0, 0, 0, 0),
  ("banner_76", 0, "map_flag_22", 0.3, 0, 0, 0, 0),
  ("banner_77", 0, "map_flag_20", 0.3, 0, 0, 0, 0),
  ("banner_78", 0, "map_flag_24", 0.3, 0, 0, 0, 0),
  ("banner_79", 0, "map_flag_25", 0.3, 0, 0, 0, 0),
  ("banner_80", 0, "map_flag_63", 0.3, 0, 0, 0, 0),
  ("banner_81", 0, "map_flag_d02", 0.3, 0, 0, 0, 0),
  ("banner_82", 0, "map_flag_d03", 0.3, 0, 0, 0, 0),
  ("banner_83", 0, "map_flag_d04", 0.3, 0, 0, 0, 0),
  ("banner_84", 0, "map_flag_d05", 0.3, 0, 0, 0, 0),
  ("banner_85", 0, "map_flag_d06", 0.3, 0, 0, 0, 0),
  ("banner_86", 0, "map_flag_d07", 0.3, 0, 0, 0, 0),
  ("banner_87", 0, "map_flag_d08", 0.3, 0, 0, 0, 0),
  ("banner_88", 0, "map_flag_d09", 0.3, 0, 0, 0, 0),
  ("banner_89", 0, "map_flag_d10", 0.3, 0, 0, 0, 0),
  ("banner_90", 0, "map_flag_d11", 0.3, 0, 0, 0, 0),
  ("banner_91", 0, "map_flag_e12", 0.3, 0, 0, 0, 0),
  ("banner_92", 0, "map_flag_e13", 0.3, 0, 0, 0, 0),
  ("banner_93", 0, "map_flag_e14", 0.3, 0, 0, 0, 0),
  ("banner_94", 0, "map_flag_e15", 0.3, 0, 0, 0, 0),
  ("banner_95", 0, "map_flag_e16", 0.3, 0, 0, 0, 0),
  ("banner_96", 0, "map_flag_e17", 0.3, 0, 0, 0, 0),
  ("banner_97", 0, "map_flag_e18", 0.3, 0, 0, 0, 0),
  ("banner_98", 0, "map_flag_e19", 0.3, 0, 0, 0, 0),
  ("banner_99", 0, "map_flag_e20", 0.3, 0, 0, 0, 0),
  ("banner_100", 0, "map_flag_e21", 0.3, 0, 0, 0, 0),
  ("banner_101", 0, "map_flag_f01", 0.3, 0, 0, 0, 0),
  ("banner_102", 0, "map_flag_f02", 0.3, 0, 0, 0, 0),
  ("banner_103", 0, "map_flag_f03", 0.3, 0, 0, 0, 0),
  ("banner_104", 0, "map_flag_f04", 0.3, 0, 0, 0, 0),
  ("banner_105", 0, "map_flag_f05", 0.3, 0, 0, 0, 0),
  ("banner_106", 0, "map_flag_f06", 0.3, 0, 0, 0, 0),
  ("banner_107", 0, "map_flag_f07", 0.3, 0, 0, 0, 0),
  ("banner_108", 0, "map_flag_f08", 0.3, 0, 0, 0, 0),
  ("banner_109", 0, "map_flag_f09", 0.3, 0, 0, 0, 0),
  ("banner_110", 0, "map_flag_f10", 0.3, 0, 0, 0, 0),
  ("banner_111", 0, "map_flag_f11", 0.3, 0, 0, 0, 0),
  ("banner_112", 0, "map_flag_57", 0.3, 0, 0, 0, 0),
  ("banner_113", 0, "map_flag_58", 0.3, 0, 0, 0, 0),
  ("banner_114", 0, "map_flag_59", 0.3, 0, 0, 0, 0),
  ("banner_115", 0, "map_flag_61", 0.3, 0, 0, 0, 0),
  ("banner_116", 0, "map_flag_62", 0.3, 0, 0, 0, 0),
  ("banner_117", 0, "map_flag_f12", 0.3, 0, 0, 0, 0),
  ("banner_118", 0, "map_flag_f13", 0.3, 0, 0, 0, 0),
  ("banner_119", 0, "map_flag_f14", 0.3, 0, 0, 0, 0),
  ("banner_120", 0, "map_flag_f15", 0.3, 0, 0, 0, 0),
  ("banner_121", 0, "map_flag_f16", 0.3, 0, 0, 0, 0),
  ("banner_122", 0, "map_flag_f17", 0.3, 0, 0, 0, 0),
  ("banner_123", 0, "map_flag_f18", 0.3, 0, 0, 0, 0),
  ("banner_124", 0, "map_flag_f19", 0.3, 0, 0, 0, 0),
  ("banner_125", 0, "map_flag_f20", 0.3, 0, 0, 0, 0),
  ("banner_126", 0, "map_flag_f21", 0.3, 0, 0, 0, 0),
]