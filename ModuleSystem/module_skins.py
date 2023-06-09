# -*- coding: UTF-8 -*-
####################################################################################################################
# Generated by Warband Module Decompiler
# All rights of the module belong to their respective owners
####################################################################################################################

from header_skins import *
from ID_particle_systems import *
####################################################################################################################
#  Each skin record contains the following fields:
#  1) Skin id: used for referencing skins.
#  2) Skin flags. Not used yet. Should be 0.
#  3) Body mesh.
#  4) Calf mesh (left one).
#  5) Hand mesh (left one).
#  6) Head mesh.
#  7) Face keys (list)
#  8) List of hair meshes.
#  9) List of beard meshes.
# 10) List of hair textures.
# 11) List of beard textures.
# 12) List of face textures.
# 13) List of voices.
# 14) Skeleton name
# 15) Scale (doesn't fully work yet)
# 16) Blood particles 1 (do not add this if you wish to use the default particles)
# 17) Blood particles 2 (do not add this if you wish to use the default particles)
# 17) Face key constraints (do not add this if you do not wish to use it)
####################################################################################################################

comp_less_than = -1;
comp_greater_than = 1;

skins = [
  (
    "american_soldier", 0,
    "man_body", "man_calf_l", "m_handL",
    "male_head",
    [
      (20, 0, 0.7, -0.6, "Chin Size"),
      (260, 0, -0.6, 1.4, "Chin Shape"),
      (10, 0, -0.5, 0.9, "Chin Forward"),
      (240, 0, 0.9, -0.8, "Jaw Width"),
      (210, 0, -0.5, 1, "Jaw Position"),
      (250, 0, 0.8, -1, "Mouth-Nose Distance"),
      (200, 0, -0.3, 1, "Mouth Width"),
      (50, 0, -1.5, 1, "Cheeks"),
      (60, 0, -0.4, 1.35, "Nose Height"),
      (70, 0, -0.6, 0.7, "Nose Width"),
      (80, 0, 1, -0.1, "Nose Size"),
      (270, 0, -0.5, 1, "Nose Shape"),
      (90, 0, -0.2, 1.4, "Nose Bridge"),
      (100, 0, -0.3, 1.5, "Cheek Bones"),
      (150, 0, -0.2, 3, "Eye Width"),
      (110, 0, 1.5, -0.9, "Eye to Eye Dist"),
      (120, 0, 1.9, -1, "Eye Shape"),
      (130, 0, -0.5, 1.1, "Eye Depth"),
      (140, 0, 1, -1.2, "Eyelids"),
      (160, 0, 1.3, -0.2, "Eyebrow Position"),
      (170, 0, -0.1, 1.9, "Eyebrow Height"),
      (220, 0, -0.1, 0.9, "Eyebrow Depth"),
      (180, 0, -1.1, 1.6, "Eyebrow Shape"),
      (230, 0, 1.2, -0.7, "Temple Width"),
      (30, 0, -0.6, 0.9, "Face Depth"),
      (40, 0, 0.9, -0.6, "Face Ratio"),
      (190, 0, 0, 0.95, "Face Width"),
      (280, 0, 0, 1, "Post-Edit"),
    ],
    ["man_hair_s", "man_hair_m", "man_hair_n", "man_hair_o", "man_hair_y10", "man_hair_y12", "man_hair_p", "man_hair_r", "man_hair_q", "man_hair_y7", "man_hair_y9", "man_hair_y11", "man_hair_y", "man_hair_y2", "man_hair_y4"],
    ["beard_e", "beard_d", "beard_k", "beard_l", "beard_i", "beard_j", "beard_z", "beard_m", "beard_n", "beard_y", "beard_p", "beard_o", "beard_v", "beard_f", "beard_b", "beard_c", "beard_t", "beard_u", "beard_r", "beard_s", "beard_a", "beard_h", "beard_g", "newbeard1", "newbeard2", "newbeard3"],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
    ["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
    [
      ("manface_young_2", 0xFFCBE0E0, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19]),
      ("manface_midage", 0xFFDFEFE1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
      ("manface_young", 0xFFD0E0E0, ["hair_blonde"], [0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("manface_young_3", 0xFFDCEDED, ["hair_blonde"], [0xff2f180e, 0xff171313, 0xff007080c]),
      ("manface_7", 0xFFC0C8C8, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_midage_2", 0xFDE4C8D8, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("manface_rugged", 0xFFB0AAB5, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_08", 0xFFB0AAB5, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_african", 0xFF807C8A, ["hair_blonde"], [0xff120808, 0xff007080c]),
    ],
    [(voice_die, "snd_man_die"),(voice_hit, "snd_man_hit"),(voice_grunt, "snd_man_grunt"),(voice_grunt_long, "snd_man_grunt_long"),(voice_yell, "snd_american_soldier_warcry"),(voice_victory, "snd_american_soldier_victory")],
    "skel_human", 1.000000,
    psys_game_blood, psys_game_blood_2,
    [
      [1.7, comp_greater_than, (1, 26),(1, 23)],
      [0.3, comp_less_than, (1, 26),(1, 23)],
      [1.7, comp_greater_than, (1, 26),(1, 24)],
      [0.3, comp_less_than, (1, 20),(1, 19)],
      [1.7, comp_greater_than, (1, 20),(1, 19)],
      [-0.7, comp_less_than, (1, 10),(-1, 11)],
      [0.7, comp_greater_than, (1, 10),(-1, 11)],
      [2.7, comp_greater_than, (1, 0),(1, 5),(1, 8),(-1, 26)],
  ]),

  (
    "american_settler", 0,
    "man_body", "man_calf_l", "m_handL",
    "male_head",
    [
      (20, 0, 0.7, -0.6, "Chin Size"),
      (260, 0, -0.6, 1.4, "Chin Shape"),
      (10, 0, -0.5, 0.9, "Chin Forward"),
      (240, 0, 0.9, -0.8, "Jaw Width"),
      (210, 0, -0.5, 1, "Jaw Position"),
      (250, 0, 0.8, -1, "Mouth-Nose Distance"),
      (200, 0, -0.3, 1, "Mouth Width"),
      (50, 0, -1.5, 1, "Cheeks"),
      (60, 0, -0.4, 1.35, "Nose Height"),
      (70, 0, -0.6, 0.7, "Nose Width"),
      (80, 0, 1, -0.1, "Nose Size"),
      (270, 0, -0.5, 1, "Nose Shape"),
      (90, 0, -0.2, 1.4, "Nose Bridge"),
      (100, 0, -0.3, 1.5, "Cheek Bones"),
      (150, 0, -0.2, 3, "Eye Width"),
      (110, 0, 1.5, -0.9, "Eye to Eye Dist"),
      (120, 0, 1.9, -1, "Eye Shape"),
      (130, 0, -0.5, 1.1, "Eye Depth"),
      (140, 0, 1, -1.2, "Eyelids"),
      (160, 0, 1.3, -0.2, "Eyebrow Position"),
      (170, 0, -0.1, 1.9, "Eyebrow Height"),
      (220, 0, -0.1, 0.9, "Eyebrow Depth"),
      (180, 0, -1.1, 1.6, "Eyebrow Shape"),
      (230, 0, 1.2, -0.7, "Temple Width"),
      (30, 0, -0.6, 0.9, "Face Depth"),
      (40, 0, 0.9, -0.6, "Face Ratio"),
      (190, 0, 0, 0.95, "Face Width"),
      (280, 0, 0, 1, "Post-Edit"),
    ],
    ["man_hair_s", "man_hair_m", "man_hair_n", "man_hair_o", "man_hair_y10", "man_hair_y12", "man_hair_p", "man_hair_r", "man_hair_q", "man_hair_y7", "man_hair_y9", "man_hair_y11", "man_hair_y", "man_hair_y2", "man_hair_y4"],
    ["beard_e", "beard_d", "beard_k", "beard_l", "beard_i", "beard_j", "beard_z", "beard_m", "beard_n", "beard_y", "beard_p", "beard_o", "beard_v", "beard_f", "beard_b", "beard_c", "beard_t", "beard_u", "beard_r", "beard_s", "beard_a", "beard_h", "beard_g", "newbeard1", "newbeard2", "newbeard3"],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
    ["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
    [
      ("manface_young_2", 0xFFCBE0E0, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19]),
      ("manface_midage", 0xFFDFEFE1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
      ("manface_young", 0xFFD0E0E0, ["hair_blonde"], [0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("manface_young_3", 0xFFDCEDED, ["hair_blonde"], [0xff2f180e, 0xff171313, 0xff007080c]),
      ("manface_7", 0xFFC0C8C8, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_midage_2", 0xFDE4C8D8, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("manface_rugged", 0xFFB0AAB5, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_08", 0xFFB0AAB5, ["hair_blonde"], [0xff171313, 0xff007080c]),
      ("manface_african", 0xFF807C8A, ["hair_blonde"], [0xff120808, 0xff007080c]),
    ],
    [(voice_die, "snd_man_die"),(voice_hit, "snd_man_hit"),(voice_grunt, "snd_man_grunt"),(voice_grunt_long, "snd_man_grunt_long"),(voice_yell, "snd_american_settler_warcry"),(voice_victory, "snd_american_settler_victory")],
    "skel_human", 1.000000,
    psys_game_blood, psys_game_blood_2,
    [
      [1.7, comp_greater_than, (1, 26),(1, 23)],
      [0.3, comp_less_than, (1, 26),(1, 23)],
      [1.7, comp_greater_than, (1, 26),(1, 24)],
      [0.3, comp_less_than, (1, 20),(1, 19)],
      [1.7, comp_greater_than, (1, 20),(1, 19)],
      [-0.7, comp_less_than, (1, 10),(-1, 11)],
      [0.7, comp_greater_than, (1, 10),(-1, 11)],
      [2.7, comp_greater_than, (1, 0),(1, 5),(1, 8),(-1, 26)],
  ]),

  (
    "mexican_man", 0,
    "man_body", "man_calf_l", "m_handL",
    "male_head",
    [
      (20, 0, 0.7, -0.6, "Chin Size"),
      (260, 0, -0.6, 1.4, "Chin Shape"),
      (10, 0, -0.5, 0.9, "Chin Forward"),
      (240, 0, 0.9, -0.8, "Jaw Width"),
      (210, 0, -0.5, 1, "Jaw Position"),
      (250, 0, 0.8, -1, "Mouth-Nose Distance"),
      (200, 0, -0.3, 1, "Mouth Width"),
      (50, 0, -1.5, 1, "Cheeks"),
      (60, 0, -0.4, 1.35, "Nose Height"),
      (70, 0, -0.6, 0.7, "Nose Width"),
      (80, 0, 1, -0.1, "Nose Size"),
      (270, 0, -0.5, 1, "Nose Shape"),
      (90, 0, -0.2, 1.4, "Nose Bridge"),
      (100, 0, -0.3, 1.5, "Cheek Bones"),
      (150, 0, -0.2, 3, "Eye Width"),
      (110, 0, 1.5, -0.9, "Eye to Eye Dist"),
      (120, 0, 1.9, -1, "Eye Shape"),
      (130, 0, -0.5, 1.1, "Eye Depth"),
      (140, 0, 1, -1.2, "Eyelids"),
      (160, 0, 1.3, -0.2, "Eyebrow Position"),
      (170, 0, -0.1, 1.9, "Eyebrow Height"),
      (220, 0, -0.1, 0.9, "Eyebrow Depth"),
      (180, 0, -1.1, 1.6, "Eyebrow Shape"),
      (230, 0, 1.2, -0.7, "Temple Width"),
      (30, 0, -0.6, 0.9, "Face Depth"),
      (40, 0, 0.9, -0.6, "Face Ratio"),
      (190, 0, 0, 0.95, "Face Width"),
      (280, 0, 0, 1, "Post-Edit"),
    ],
    ["man_hair_s", "man_hair_m", "man_hair_n", "man_hair_o", "man_hair_p", "man_hair_r", "man_hair_q", "man_hair_y", "man_hair_y2", "man_hair_y4", "man_hair_y5", "man_hair_y7", "man_hair_y9", "man_hair_y8", "man_hair_y10", "man_hair_y11", "man_hair_y12"],
    ["beard_z", "beard_y", "beard_v", "beard_q", "beard_c", "beard_b", "beard_i"],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
    ["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
    [
      ("manface_mexican1", 0xFF807C8A, ["hair_blonde"], [0xff120808, 0xff007080c]),
      ("manface_mexican2", 0xFF807C8A, ["hair_blonde"], [0xff120808, 0xff007080c]),
      ("manface_mexican3", 0xFF807C8A, ["hair_blonde"], [0xff120808, 0xff007080c]),
      ("manface_mexican4", 0xFF807C8A, ["hair_blonde"], [0xff120808, 0xff007080c]),
      ("manface_mexican5", 0xFF807C8A, ["hair_blonde"], [0xff120808, 0xff007080c]),
    ],
    [(voice_die, "snd_man_die"),(voice_hit, "snd_man_hit"),(voice_grunt, "snd_man_grunt"),(voice_grunt_long, "snd_man_grunt_long"),(voice_yell, "snd_mexican_warcry"),(voice_victory, "snd_mexican_victory")],
    "skel_human", 1.000000,
    psys_game_blood, psys_game_blood_2,
    [
      [1.7, comp_greater_than, (1, 26),(1, 23)],
      [0.3, comp_less_than, (1, 26),(1, 23)],
      [1.7, comp_greater_than, (1, 26),(1, 24)],
      [0.3, comp_less_than, (1, 20),(1, 19)],
      [1.7, comp_greater_than, (1, 20),(1, 19)],
      [-0.7, comp_less_than, (1, 10),(-1, 11)],
      [0.7, comp_greater_than, (1, 10),(-1, 11)],
      [2.7, comp_greater_than, (1, 0),(1, 5),(1, 8),(-1, 26)],
  ]),

  (
    "indian_man", 0,
    "indian_body", "man_calf_l", "m_handL",
    "male_head",
    [
      (20, 0, 0.7, -0.6, "Chin Size"),
      (260, 0, -0.6, 1.4, "Chin Shape"),
      (10, 0, -0.5, 0.9, "Chin Forward"),
      (240, 0, 0.9, -0.8, "Jaw Width"),
      (210, 0, -0.5, 1, "Jaw Position"),
      (250, 0, 0.8, -1, "Mouth-Nose Distance"),
      (200, 0, -0.3, 1, "Mouth Width"),
      (50, 0, -1.5, 1, "Cheeks"),
      (60, 0, -0.4, 1.35, "Nose Height"),
      (70, 0, -0.6, 0.7, "Nose Width"),
      (80, 0, 1, -0.1, "Nose Size"),
      (270, 0, -0.5, 1, "Nose Shape"),
      (90, 0, -0.2, 1.4, "Nose Bridge"),
      (100, 0, -0.3, 1.5, "Cheek Bones"),
      (150, 0, -0.2, 3, "Eye Width"),
      (110, 0, 1.5, -0.9, "Eye to Eye Dist"),
      (120, 0, 1.9, -1, "Eye Shape"),
      (130, 0, -0.5, 1.1, "Eye Depth"),
      (140, 0, 1, -1.2, "Eyelids"),
      (160, 0, 1.3, -0.2, "Eyebrow Position"),
      (170, 0, -0.1, 1.9, "Eyebrow Height"),
      (220, 0, -0.1, 0.9, "Eyebrow Depth"),
      (180, 0, -1.1, 1.6, "Eyebrow Shape"),
      (230, 0, 1.2, -0.7, "Temple Width"),
      (30, 0, -0.6, 0.9, "Face Depth"),
      (40, 0, 0.9, -0.6, "Face Ratio"),
      (190, 0, 0, 0.95, "Face Width"),
      (280, 0, 0, 1, "Post-Edit"),
    ],
    ["apache_hair_a", "man_hair_r", "man_hair_p", "man_hair_q"],
    [],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
    ["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
    [
      ("manface_sioux", 0xFF8A8A8A, ["hair_blonde"], [0xff120808, 0xff007080c]),
      ("manface_iroquois", 0xFF8A8A8A, ["hair_blonde"], [0xff120808, 0xff007080c]),
      ("manface_iroquois2", 0xFF8A8A8A, ["hair_blonde"], [0xff120808, 0xff007080c]),
      ("manface_iroquois3", 0xFF8A8A8A, ["hair_blonde"], [0xff120808, 0xff007080c]),
      ("manface_iroquois4", 0xFF8A8A8A, ["hair_blonde"], [0xff120808, 0xff007080c]),
      ("manface_iroquois5", 0xFF8A8A8A, ["hair_blonde"], [0xff120808, 0xff007080c]),
      ("manface_iroquois6", 0xFF8A8A8A, ["hair_blonde"], [0xff120808, 0xff007080c]),
    ],
    [(voice_die, "snd_man_die"),(voice_hit, "snd_man_hit"),(voice_grunt, "snd_man_grunt"),(voice_grunt_long, "snd_man_grunt_long"),(voice_yell, "snd_indian_warcry"),(voice_victory, "snd_indian_victory")],
    "skel_human", 1.000000,
    psys_game_blood, psys_game_blood_2,
    [
      [1.7, comp_greater_than, (1, 26),(1, 23)],
      [0.3, comp_less_than, (1, 26),(1, 23)],
      [1.7, comp_greater_than, (1, 26),(1, 24)],
      [0.3, comp_less_than, (1, 20),(1, 19)],
      [1.7, comp_greater_than, (1, 20),(1, 19)],
      [-0.7, comp_less_than, (1, 10),(-1, 11)],
      [0.7, comp_greater_than, (1, 10),(-1, 11)],
      [2.7, comp_greater_than, (1, 0),(1, 5),(1, 8),(-1, 26)],
  ]),

  (
    "american_woman", 1,
    "woman_body", "woman_calf_l", "female_hand_L",
    "female_head",
    [
      (230, 0, 0.8, -1, "Chin Size"),
      (220, 0, -1, 1, "Chin Shape"),
      (10, 0, -1.2, 1, "Chin Forward"),
      (20, 0, -0.6, 1.2, "Jaw Width"),
      (40, 0, -0.7, 1, "Jaw Position"),
      (270, 0, 0.9, -0.9, "Mouth-Nose Distance"),
      (30, 0, -0.5, 1, "Mouth Width"),
      (50, 0, -0.5, 1, "Cheeks"),
      (60, 0, -0.5, 1, "Nose Height"),
      (70, 0, -0.5, 1.1, "Nose Width"),
      (80, 0, 1.5, -0.3, "Nose Size"),
      (240, 0, -1, 0.8, "Nose Shape"),
      (90, 0, 0, 1.1, "Nose Bridge"),
      (100, 0, -0.5, 1.5, "Cheek Bones"),
      (150, 0, -0.4, 1, "Eye Width"),
      (110, 0, 1, 0, "Eye to Eye Dist"),
      (120, 0, -0.2, 1, "Eye Shape"),
      (130, 0, -0.1, 1.6, "Eye Depth"),
      (140, 0, -0.2, 1, "Eyelids"),
      (160, 0, -0.2, 1.2, "Eyebrow Position"),
      (170, 0, -0.2, 0.7, "Eyebrow Height"),
      (250, 0, -0.4, 0.9, "Eyebrow Depth"),
      (180, 0, -1.5, 1.2, "Eyebrow Shape"),
      (260, 0, 1, -0.7, "Temple Width"),
      (200, 0, -0.5, 1, "Face Depth"),
      (210, 0, -0.5, 0.9, "Face Ratio"),
      (190, 0, -0.4, 0.8, "Face Width"),
      (280, 0, 0, 1, "Post-Edit"),
    ],
    ["woman_hair_p", "woman_hair_n", "woman_hair_o", "woman_hair_q", "woman_hair_r", "woman_hair_t", "woman_hair_s"],
    [],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
    [],
    [
      ("womanface_young", 0xFFE3E8EF, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
      ("womanface_b", 0xFFDFDFDF, ["hair_blonde"], [0xffa5481f, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("womanface_a", 0xFFE8DFE5, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("womanface_african", 0xFF808080, ["hair_blonde"], [0xff120808, 0xff007080c]),
      ("womanface_african_2", 0xFF808080, ["hair_blonde"], [0xff120808, 0xff007080c]),
      ("womanface_04", 0xFFDFDFDF, ["hair_blonde"], [0xffa5481f, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("womanface_05", 0xFFE3E8EF, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
      ("womanface_06", 0xFFE8DFE5, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("womanface_07", 0xFFDFDFDF, ["hair_blonde"], [0xffa5481f, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("womanface_08", 0xFFE8DFE5, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("womanface_09", 0xFFDFDFDF, ["hair_blonde"], [0xffa5481f, 0xff502a19, 0xff19100c, 0xff0c0d19]),
    ],
    [(voice_die, "snd_woman_die"),(voice_hit, "snd_woman_hit"),(voice_grunt, "snd_woman_grunt"),(voice_grunt_long, "snd_woman_grunt_long"),(voice_yell, "snd_woman_yell"),(voice_victory, "snd_woman_victory")],
    "skel_human", 1.000000,
    psys_game_blood, psys_game_blood_2,
    [
  ]),

  (
    "mexican_woman", 1,
    "woman_body", "woman_calf_l", "female_hand_L",
    "female_head",
    [
      (230, 0, 0.8, -1, "Chin Size"),
      (220, 0, -1, 1, "Chin Shape"),
      (10, 0, -1.2, 1, "Chin Forward"),
      (20, 0, -0.6, 1.2, "Jaw Width"),
      (40, 0, -0.7, 1, "Jaw Position"),
      (270, 0, 0.9, -0.9, "Mouth-Nose Distance"),
      (30, 0, -0.5, 1, "Mouth Width"),
      (50, 0, -0.5, 1, "Cheeks"),
      (60, 0, -0.5, 1, "Nose Height"),
      (70, 0, -0.5, 1.1, "Nose Width"),
      (80, 0, 1.5, -0.3, "Nose Size"),
      (240, 0, -1, 0.8, "Nose Shape"),
      (90, 0, 0, 1.1, "Nose Bridge"),
      (100, 0, -0.5, 1.5, "Cheek Bones"),
      (150, 0, -0.4, 1, "Eye Width"),
      (110, 0, 1, 0, "Eye to Eye Dist"),
      (120, 0, -0.2, 1, "Eye Shape"),
      (130, 0, -0.1, 1.6, "Eye Depth"),
      (140, 0, -0.2, 1, "Eyelids"),
      (160, 0, -0.2, 1.2, "Eyebrow Position"),
      (170, 0, -0.2, 0.7, "Eyebrow Height"),
      (250, 0, -0.4, 0.9, "Eyebrow Depth"),
      (180, 0, -1.5, 1.2, "Eyebrow Shape"),
      (260, 0, 1, -0.7, "Temple Width"),
      (200, 0, -0.5, 1, "Face Depth"),
      (210, 0, -0.5, 0.9, "Face Ratio"),
      (190, 0, -0.4, 0.8, "Face Width"),
      (280, 0, 0, 1, "Post-Edit"),
    ],
    ["woman_hair_p", "woman_hair_n", "woman_hair_o", "woman_hair_q", "woman_hair_r", "woman_hair_t", "woman_hair_s"],
    [],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
    [],
    [
      ("womanface_brown", 0xFFAF9F7E, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c]),
      ("womanface_mexican_01", 0xFFAF9F7E, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c]),
    ],
    [(voice_die, "snd_woman_die"),(voice_hit, "snd_woman_hit"),(voice_grunt, "snd_woman_grunt"),(voice_grunt_long, "snd_woman_grunt_long"),(voice_yell, "snd_woman_yell"),(voice_victory, "snd_woman_victory")],
    "skel_human", 1.000000,
    psys_game_blood, psys_game_blood_2,
    [
  ]),

  (
    "indian_woman", 1,
    "woman_body", "woman_calf_l", "female_hand_L",
    "female_head",
    [
      (230, 0, 0.8, -1, "Chin Size"),
      (220, 0, -1, 1, "Chin Shape"),
      (10, 0, -1.2, 1, "Chin Forward"),
      (20, 0, -0.6, 1.2, "Jaw Width"),
      (40, 0, -0.7, 1, "Jaw Position"),
      (270, 0, 0.9, -0.9, "Mouth-Nose Distance"),
      (30, 0, -0.5, 1, "Mouth Width"),
      (50, 0, -0.5, 1, "Cheeks"),
      (60, 0, -0.5, 1, "Nose Height"),
      (70, 0, -0.5, 1.1, "Nose Width"),
      (80, 0, 1.5, -0.3, "Nose Size"),
      (240, 0, -1, 0.8, "Nose Shape"),
      (90, 0, 0, 1.1, "Nose Bridge"),
      (100, 0, -0.5, 1.5, "Cheek Bones"),
      (150, 0, -0.4, 1, "Eye Width"),
      (110, 0, 1, 0, "Eye to Eye Dist"),
      (120, 0, -0.2, 1, "Eye Shape"),
      (130, 0, -0.1, 1.6, "Eye Depth"),
      (140, 0, -0.2, 1, "Eyelids"),
      (160, 0, -0.2, 1.2, "Eyebrow Position"),
      (170, 0, -0.2, 0.7, "Eyebrow Height"),
      (250, 0, -0.4, 0.9, "Eyebrow Depth"),
      (180, 0, -1.5, 1.2, "Eyebrow Shape"),
      (260, 0, 1, -0.7, "Temple Width"),
      (200, 0, -0.5, 1, "Face Depth"),
      (210, 0, -0.5, 0.9, "Face Ratio"),
      (190, 0, -0.4, 0.8, "Face Width"),
      (280, 0, 0, 1, "Post-Edit"),
    ],
    ["woman_hair_p", "woman_hair_n", "woman_hair_o", "woman_hair_q", "woman_hair_r", "woman_hair_t"],
    [],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
    [],
    [
      ("womanface_indian_01", 0xFFAF9F7E, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c]),
      ("womanface_indian_02", 0xFFAF9F7E, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c]),
    ],
    [(voice_die, "snd_woman_die"),(voice_hit, "snd_woman_hit"),(voice_grunt, "snd_woman_grunt"),(voice_grunt_long, "snd_woman_grunt_long"),(voice_yell, "snd_woman_yell"),(voice_victory, "snd_woman_victory")],
    "skel_human", 1.000000,
    psys_game_blood, psys_game_blood_2,
    [
  ]),

  (
    "cheat", 0,
    "man_body", "man_calf_l", "m_handL",
    "male_head",
    [
      (20, 0, 0.7, -0.6, "Chin Size"),
      (260, 0, -0.6, 1.4, "Chin Shape"),
      (10, 0, -0.5, 0.9, "Chin Forward"),
      (240, 0, 0.9, -0.8, "Jaw Width"),
      (210, 0, -0.5, 1, "Jaw Position"),
      (250, 0, 0.8, -1, "Mouth-Nose Distance"),
      (200, 0, -0.3, 1, "Mouth Width"),
      (50, 0, -1.5, 1, "Cheeks"),
      (60, 0, -0.4, 1.35, "Nose Height"),
      (70, 0, -0.6, 0.7, "Nose Width"),
      (80, 0, 1, -0.1, "Nose Size"),
      (270, 0, -0.5, 1, "Nose Shape"),
      (90, 0, -0.2, 1.4, "Nose Bridge"),
      (100, 0, -0.3, 1.5, "Cheek Bones"),
      (150, 0, -0.2, 3, "Eye Width"),
      (110, 0, 1.5, -0.9, "Eye to Eye Dist"),
      (120, 0, 1.9, -1, "Eye Shape"),
      (130, 0, -0.5, 1.1, "Eye Depth"),
      (140, 0, 1, -1.2, "Eyelids"),
      (160, 0, 1.3, -0.2, "Eyebrow Position"),
      (170, 0, -0.1, 1.9, "Eyebrow Height"),
      (220, 0, -0.1, 0.9, "Eyebrow Depth"),
      (180, 0, -1.1, 1.6, "Eyebrow Shape"),
      (230, 0, 1.2, -0.7, "Temple Width"),
      (30, 0, -0.6, 0.9, "Face Depth"),
      (40, 0, 0.9, -0.6, "Face Ratio"),
      (190, 0, 0, 0.95, "Face Width"),
      (280, 0, 0, 1, "Post-Edit"),
    ],
    ["man_hair_s", "man_hair_m", "man_hair_n", "man_hair_o", "man_hair_p", "man_hair_r", "man_hair_q", "man_hair_y", "man_hair_y2", "man_hair_y4", "man_hair_y5", "man_hair_y7", "man_hair_y9", "man_hair_y8", "man_hair_y10", "man_hair_y11", "man_hair_y12"],
    ["beard_na", "beard_nb", "beard_nc", "beard_g", "beard_f", "beard_v", "beard_i"],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
    ["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
    [
      ("manface_eastwood", 0xFDE4C8D8, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("manface_clown", 0xFDE4C8D8, ["hair_blonde"], [0xffcb0e0e, 0xff19100c, 0xff0c0d19]),
    ],
    [(voice_die, "snd_man_die"),(voice_hit, "snd_man_hit"),(voice_grunt, "snd_man_grunt"),(voice_grunt_long, "snd_man_grunt_long"),(voice_yell, "snd_man_yell"),(voice_victory, "snd_man_victory")],
    "skel_human", 1.000000,
    psys_game_blood, psys_game_blood_2,
    [
      [1.7, comp_greater_than, (1, 26),(1, 23)],
      [0.3, comp_less_than, (1, 26),(1, 23)],
      [1.7, comp_greater_than, (1, 26),(1, 24)],
      [0.3, comp_less_than, (1, 20),(1, 19)],
      [1.7, comp_greater_than, (1, 20),(1, 19)],
      [-0.7, comp_less_than, (1, 10),(-1, 11)],
      [0.7, comp_greater_than, (1, 10),(-1, 11)],
      [2.7, comp_greater_than, (1, 0),(1, 5),(1, 8),(-1, 26)],
  ]),

  (
    "undead", 0,
    "man_body", "man_calf_l", "m_handL",
    "male_head",
    [
      (20, 0, 0.7, -0.6, "Chin Size"),
      (260, 0, -0.6, 1.4, "Chin Shape"),
      (10, 0, -0.5, 0.9, "Chin Forward"),
      (240, 0, 0.9, -0.8, "Jaw Width"),
      (210, 0, -0.5, 1, "Jaw Position"),
      (250, 0, 0.8, -1, "Mouth-Nose Distance"),
      (200, 0, -0.3, 1, "Mouth Width"),
      (50, 0, -1.5, 1, "Cheeks"),
      (60, 0, -0.4, 1.35, "Nose Height"),
      (70, 0, -0.6, 0.7, "Nose Width"),
      (80, 0, 1, -0.1, "Nose Size"),
      (270, 0, -0.5, 1, "Nose Shape"),
      (90, 0, -0.2, 1.4, "Nose Bridge"),
      (100, 0, -0.3, 1.5, "Cheek Bones"),
      (150, 0, -0.2, 3, "Eye Width"),
      (110, 0, 1.5, -0.9, "Eye to Eye Dist"),
      (120, 0, 1.9, -1, "Eye Shape"),
      (130, 0, -0.5, 1.1, "Eye Depth"),
      (140, 0, 1, -1.2, "Eyelids"),
      (160, 0, 1.3, -0.2, "Eyebrow Position"),
      (170, 0, -0.1, 1.9, "Eyebrow Height"),
      (220, 0, -0.1, 0.9, "Eyebrow Depth"),
      (180, 0, -1.1, 1.6, "Eyebrow Shape"),
      (230, 0, 1.2, -0.7, "Temple Width"),
      (30, 0, -0.6, 0.9, "Face Depth"),
      (40, 0, 0.9, -0.6, "Face Ratio"),
      (190, 0, 0, 0.95, "Face Width"),
      (280, 0, 0, 1, "Post-Edit"),
    ],
    ["man_hair_s", "man_hair_m", "man_hair_n", "man_hair_o", "man_hair_y10", "man_hair_y12", "man_hair_p", "man_hair_r", "man_hair_q", "man_hair_y7", "man_hair_y9", "man_hair_y11", "man_hair_y", "man_hair_y2", "man_hair_y4"],
    ["beard_e", "beard_d", "beard_k", "beard_l", "beard_i", "beard_j", "beard_z", "beard_m", "beard_n", "beard_y", "beard_p", "beard_o", "beard_v", "beard_f", "beard_b", "beard_c", "beard_t", "beard_u", "beard_r", "beard_s", "beard_a", "beard_h", "beard_g", "newbeard1", "newbeard2", "newbeard3"],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
    ["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
    [
      ("manface_undead_a", 0xFFCBE0E0, ["hair_blonde"], [0xffffffff, 0xffffffff, 0xffffffff]),
      ("manface_undead_b", 0xFFDFEFE1, ["hair_blonde"], [0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff]),
    ],
    [(voice_die, "snd_man_die"),(voice_hit, "snd_man_hit"),(voice_grunt, "snd_man_grunt"),(voice_grunt_long, "snd_man_grunt_long"),(voice_yell, "snd_man_yell"),(voice_victory, "snd_man_victory")],
    "skel_human", 1.000000,
    psys_game_blood, psys_game_blood_2,
    [
  ]),

  (
    "undead2", 0,
    "undead_body", "undead_calf_l", "undead_handnewL",
    "undead_head",
    [
      (20, 0, 0.7, -0.6, "Chin Size"),
      (260, 0, -0.6, 1.4, "Chin Shape"),
      (10, 0, -0.5, 0.9, "Chin Forward"),
      (240, 0, 0.9, -0.8, "Jaw Width"),
      (210, 0, -0.5, 1, "Jaw Position"),
      (250, 0, 0.8, -1, "Mouth-Nose Distance"),
      (200, 0, -0.3, 1, "Mouth Width"),
      (50, 0, -1.5, 1, "Cheeks"),
      (60, 0, -0.4, 1.35, "Nose Height"),
      (70, 0, -0.6, 0.7, "Nose Width"),
      (80, 0, 1, -0.1, "Nose Size"),
      (270, 0, -0.5, 1, "Nose Shape"),
      (90, 0, -0.2, 1.4, "Nose Bridge"),
      (100, 0, -0.3, 1.5, "Cheek Bones"),
      (150, 0, -0.2, 3, "Eye Width"),
      (110, 0, 1.5, -0.9, "Eye to Eye Dist"),
      (120, 0, 1.9, -1, "Eye Shape"),
      (130, 0, -0.5, 1.1, "Eye Depth"),
      (140, 0, 1, -1.2, "Eyelids"),
      (160, 0, 1.3, -0.2, "Eyebrow Position"),
      (170, 0, -0.1, 1.9, "Eyebrow Height"),
      (220, 0, -0.1, 0.9, "Eyebrow Depth"),
      (180, 0, -1.1, 1.6, "Eyebrow Shape"),
      (230, 0, 1.2, -0.7, "Temple Width"),
      (30, 0, -0.6, 0.9, "Face Depth"),
      (40, 0, 0.9, -0.6, "Face Ratio"),
      (190, 0, 0, 0.95, "Face Width"),
      (280, 0, 0, 1, "Post-Edit"),
    ],
    [],
    [],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
    ["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
    [
      ("manface_undead_c", 0xFFCBE0E0, ["hair_blonde"], [0xffffffff, 0xffffffff, 0xffffffff]),
      ("manface_undead_d", 0xFFDFEFE1, ["hair_blonde"], [0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff]),
    ],
    [(voice_die, "snd_man_die"),(voice_hit, "snd_man_hit"),(voice_grunt, "snd_man_grunt"),(voice_grunt_long, "snd_man_grunt_long"),(voice_yell, "snd_man_yell"),(voice_victory, "snd_man_victory")],
    "skel_human", 1.000000,
    psys_game_blood, psys_game_blood_2,
    [
  ]),

  (
    "undead2_no_head", 0,
    "undead_body", "undead_calf_l", "undead_handnewL",
    "nothing",
    [
      (20, 0, 0.7, -0.6, "Chin Size"),
      (260, 0, -0.6, 1.4, "Chin Shape"),
      (10, 0, -0.5, 0.9, "Chin Forward"),
      (240, 0, 0.9, -0.8, "Jaw Width"),
      (210, 0, -0.5, 1, "Jaw Position"),
      (250, 0, 0.8, -1, "Mouth-Nose Distance"),
      (200, 0, -0.3, 1, "Mouth Width"),
      (50, 0, -1.5, 1, "Cheeks"),
      (60, 0, -0.4, 1.35, "Nose Height"),
      (70, 0, -0.6, 0.7, "Nose Width"),
      (80, 0, 1, -0.1, "Nose Size"),
      (270, 0, -0.5, 1, "Nose Shape"),
      (90, 0, -0.2, 1.4, "Nose Bridge"),
      (100, 0, -0.3, 1.5, "Cheek Bones"),
      (150, 0, -0.2, 3, "Eye Width"),
      (110, 0, 1.5, -0.9, "Eye to Eye Dist"),
      (120, 0, 1.9, -1, "Eye Shape"),
      (130, 0, -0.5, 1.1, "Eye Depth"),
      (140, 0, 1, -1.2, "Eyelids"),
      (160, 0, 1.3, -0.2, "Eyebrow Position"),
      (170, 0, -0.1, 1.9, "Eyebrow Height"),
      (220, 0, -0.1, 0.9, "Eyebrow Depth"),
      (180, 0, -1.1, 1.6, "Eyebrow Shape"),
      (230, 0, 1.2, -0.7, "Temple Width"),
      (30, 0, -0.6, 0.9, "Face Depth"),
      (40, 0, 0.9, -0.6, "Face Ratio"),
      (190, 0, 0, 0.95, "Face Width"),
      (280, 0, 0, 1, "Post-Edit"),
    ],
    [],
    [],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
    ["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
    [
      ("manface_undead_c", 0xFFCBE0E0, ["hair_blonde"], [0xffffffff, 0xffffffff, 0xffffffff]),
      ("manface_undead_d", 0xFFDFEFE1, ["hair_blonde"], [0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff]),
    ],
    [(voice_die, "snd_man_die"),(voice_hit, "snd_man_hit"),(voice_grunt, "snd_man_grunt"),(voice_grunt_long, "snd_man_grunt_long"),(voice_yell, "snd_man_yell"),(voice_victory, "snd_man_victory")],
    "skel_human", 1.000000,
    psys_game_blood, psys_game_blood_2,
    [
  ]),

  (
    "invisible_mute", 0,
    "man_body", "man_calf_l", "m_handL",
    "male_head",
    [
      (20, 0, 0.7, -0.6, "Chin Size"),
      (260, 0, -0.6, 1.4, "Chin Shape"),
      (10, 0, -0.5, 0.9, "Chin Forward"),
      (240, 0, 0.9, -0.8, "Jaw Width"),
      (210, 0, -0.5, 1, "Jaw Position"),
      (250, 0, 0.8, -1, "Mouth-Nose Distance"),
      (200, 0, -0.3, 1, "Mouth Width"),
      (50, 0, -1.5, 1, "Cheeks"),
      (60, 0, -0.4, 1.35, "Nose Height"),
      (70, 0, -0.6, 0.7, "Nose Width"),
      (80, 0, 1, -0.1, "Nose Size"),
      (270, 0, -0.5, 1, "Nose Shape"),
      (90, 0, -0.2, 1.4, "Nose Bridge"),
      (100, 0, -0.3, 1.5, "Cheek Bones"),
      (150, 0, -0.2, 3, "Eye Width"),
      (110, 0, 1.5, -0.9, "Eye to Eye Dist"),
      (120, 0, 1.9, -1, "Eye Shape"),
      (130, 0, -0.5, 1.1, "Eye Depth"),
      (140, 0, 1, -1.2, "Eyelids"),
      (160, 0, 1.3, -0.2, "Eyebrow Position"),
      (170, 0, -0.1, 1.9, "Eyebrow Height"),
      (220, 0, -0.1, 0.9, "Eyebrow Depth"),
      (180, 0, -1.1, 1.6, "Eyebrow Shape"),
      (230, 0, 1.2, -0.7, "Temple Width"),
      (30, 0, -0.6, 0.9, "Face Depth"),
      (40, 0, 0.9, -0.6, "Face Ratio"),
      (190, 0, 0, 0.95, "Face Width"),
      (280, 0, 0, 1, "Post-Edit"),
    ],
    [],
    [],
    ["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
    ["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
    [
      ("manface_young_2", 0xFFCBE0E0, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19]),
    ],
    [(voice_die, "snd_nothing"),(voice_hit, "snd_nothing"),(voice_grunt, "snd_nothing"),(voice_grunt_long, "snd_nothing"),(voice_yell, "snd_nothing"),(voice_victory, "snd_nothing")],
    "skel_human", 1.000000,
    psys_nothing, psys_nothing,
    [
      [1.7, comp_greater_than, (1, 26),(1, 23)],
      [0.3, comp_less_than, (1, 26),(1, 23)],
      [1.7, comp_greater_than, (1, 26),(1, 24)],
      [0.3, comp_less_than, (1, 20),(1, 19)],
      [1.7, comp_greater_than, (1, 20),(1, 19)],
      [-0.7, comp_less_than, (1, 10),(-1, 11)],
      [0.7, comp_greater_than, (1, 10),(-1, 11)],
      [2.7, comp_greater_than, (1, 0),(1, 5),(1, 8),(-1, 26)],
  ]),

]