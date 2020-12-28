import os

import jieba
from jieba import posseg as pseg
import codecs
import pandas as pd


def read_novels_role_count(role_path, novels_path):
    """

    :param role_path: 角色字典地址
    :param novels_path: 小说地址
    :return:
    """
    jieba.load_userdict(role_path)
    line_names = []
    with codecs.open(novels_path, 'r', 'utf-8') as f:
        novels_lines = f.readlines()

    for line in novels_lines:
        poss = pseg.cut(line)
        line_names.append([])
        for w in poss:
            if w.flag != "nr" or w.word in role_name_list:
                continue
            line_names[-1].append(w.word)
            if names.get(w.word) is None:
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1

    # 构建人物关系
    for line in line_names:
        for name1 in line:
            for name2 in line:
                if name1 == name2:
                    continue
                if relationships[name1].get(name2) is None:
                    relationships[name1][name2] = 1
                else:
                    relationships[name1][name2] += 1


def write_file():
    # 人物出现次数
    with codecs.open("./jinyong_novels_library/report/jinyong.csv", "a+", "utf-8") as f:
        f.write("Id,Label,Count\r\n")
        for name, number in names.items():
            f.write(name + "," + name + "," + str(number) + "\r\n")

    # 关系
    with codecs.open("./jinyong_novels_library/report/jinyong_relationship.csv", "a+", "utf-8") as f:
        f.write("Source,Target,Weight\r\n")
        for name, edges in relationships.items():
            for v, w in edges.items():
                f.write(name + "," + v + "," + str(w) + "\n")


if __name__ == '__main__':
    roles_path = './jinyong_novels_library/roles.txt'

    # 角色名字列表
    role_data = pd.read_csv(roles_path, header=None)
    role_name_list = [role[0].split()[0] for role in role_data.values.tolist()]

    # 人物关系
    relationships = {}

    # 角色出现的次数
    names = {}
    novels_list = os.listdir("./jinyong_novels_library")
    for novel_name in novels_list:
        if novel_name in ["roles.txt", "人名.txt"] or not novel_name.endswith(".txt"):
            print(novel_name)
            continue
    # print(novels_list)
        novel_path = "./jinyong_novels_library/{}".format(novel_name)
        read_novels_role_count(roles_path, novel_path)
    write_file()