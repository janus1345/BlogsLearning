# -*- coding: utf-8 -*-

import jieba 

joy_of_life_path = ""
with open(joy _of_life_path, 'r', encoding='utf-8') as file:
    joy_of_life_txt = file.read()
jieba.cut(joy_of_life_txt, cut_all=True)