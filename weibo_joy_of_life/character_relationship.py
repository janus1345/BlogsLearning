# -*- coding: utf-8 -*-

import jieba


def jieba_cut():
    """
    使用jieba中的 全模式 切割了小说
    :return:
    """
    joy_of_life_path = "./novels/joy_of_lift.txt"
    with open(joy_of_life_path, 'r', encoding='GB18030') as file:
        joy_of_life_txt = file.read()
    seg_list = jieba.cut(joy_of_life_txt, cut_all=True, HMM=False)
    seg_list_strip = [i.strip() for i in seg_list if (i.strip() and
                                                      (i.strip() not in ["。", "，", "", "，“", "“", "。”",
                                                                         "：“", ":", "“"]))]
    print("Full Mode: ", "/".join(seg_list_strip))


def synonymous_names(synonymous_dict_path):
    """
    使用提前准备好的 人物名称和他们的别名 建立字典
    :param synonymous_dict_path:
    :return:
    """
    synonymous_dict = {}
    with open(synonymous_dict_path, 'r', encoding='GB18030') as f:
        lines = f.readlines()
    for l in lines:
        synonymous_dict[l.split(" ")[0]] = l.split(" ")[1]
    return synonymous_dict


