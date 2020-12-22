import codecs
import jieba
import jieba.posseg as pseg
import pandas as pd


def read_novels_role_count():
    """
    读取小说全本 统计人物出场次数
    :return:
    """
    # 加载角色字典
    role_path = "./library_joy_of_life/role.txt"
    jieba.load_userdict(role_path)

    novels_path = "./library_joy_of_life/joy_of_life.txt"
    line_names = []
    with codecs.open(novels_path, 'r', 'utf-8') as f:
        novels_lines = f.readlines()

    for line in novels_lines:
        poss = pseg.cut(line)
        line_names.append([])
        for w in poss:
            if w.flag != "nr" or len(w.word) < 2 or len(w.word) > 4 or w.word not in role_name_list:
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
    with codecs.open("./library_joy_of_life/qyn_role.csv", "a+", "utf-8") as f:
        f.write("Id,Label,Count\r\n")
        for name, number in names.items():
            f.write(name + "," + name + "," + str(number) + "\r\n")

    # 关系
    with codecs.open("./library_joy_of_life/qyn_relationship.csv", "a+", "utf-8") as f:
        f.write("Source,Target,Weight\r\n")
        for name, edges in relationships.items():
            for v, w in edges.items():
                f.write(name + "," + v + "," + str(w) + "\n")


if __name__ == '__main__':
    # 返回角色的 名字的 列表
    role_data = pd.read_csv("./library_joy_of_life/role.txt", header=None)
    # tolist 返回list结构值
    role_name_list = [i[0].split()[0] for i in role_data.values.tolist()]

    # 角色出现的次数
    names = {}
    # 人物关系
    relationships = {}

    read_novels_role_count()
    write_file()