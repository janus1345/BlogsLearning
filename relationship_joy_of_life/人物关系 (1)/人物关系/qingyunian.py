import codecs

import jieba
import jieba.posseg as pseg
import pandas as pd


names = {}    
relationships = {}  
line_names = []
# 加载角色字典
jieba.load_userdict("role.txt")
role_data = pd.read_csv("role.txt", header=None)
mylist = [k[0].split(" ")[0] for k in role_data.values.tolist()]

# 读取小说全本，统计人物出场次数
with codecs.open("joy_of_life.txt", "r", "utf-8") as f:
    # 按行读取
    for line in f.readlines():
        # 分词
        poss = pseg.cut(line)
        line_names.append([])        
        for w in poss:
            if w.flag != 'nr' or len(w.word) >4 or len(w.word)<2 or w.word not in mylist:
                continue
            line_names[-1].append(w.word) 
            if names.get(w.word) is None:
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1
print(line_names)

# 构建人物关系
for line in line_names:
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                relationships[name1][name2]= 1
            else:
                relationships[name1][name2] = relationships[name1][name2]+ 1

# 输出
with codecs.open("qyn_node.csv", "a+", "utf-8") as f:
    f.write("Id,Label,Weight\r\n")
    for name, times in names.items():
        f.write(name + "," + name + "," + str(times) + "\r\n")


with codecs.open("qyn_edge.csv", "a+", "utf-8") as f:
    f.write("Source,Target,Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            f.write(name + "," + v + "," + str(w) + "\n")