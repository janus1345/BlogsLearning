# -*- coding: utf-8 -*-
# @Time : 2020/12/29 16:36
# @Author : tanyao@seefun.cn
# @FileName: relationships_graph.py
# @Software: PyCharm
# @desc:
import pandas as pd
from pyecharts.charts import Graph
from pyecharts import options as opts


def drawing_graph():
    node_data = pd.read_csv("./jinyong_novels_library/report/jinyong.csv")
    relationship_data = pd.read_csv("./jinyong_novels_library/report/jinyong_relationship.csv")

    node_data_list = node_data.values.tolist()
    relationship_data_list = relationship_data.values.tolist()

    nodes = []

    for node in node_data_list:
        if node[0] == "韦小宝":
            node[2] = node[2] / 10
        if node[0] == "令狐冲":
            node[2] = node[2] / 10
        if node[0] == "杨过":
            node[2] = node[2] / 10
        if node[0] == "郭靖":
            node[2] = node[2] / 10
        if node[0] == "黄蓉":
            node[2] = node[2] / 10
        if node[0] == "张无忌":
            node[2] = node[2] / 10
        if node[0] == "段誉":
            node[2] = node[2] / 10
        if node[0] == "袁承志":
            node[2] = node[2] / 2

        nodes.append({"name": node[0], "symbolSize": node[2] / 30})

    links = []
    for link in relationship_data_list:
        links.append({'source': link[0], 'target': link[1], 'value': link[2]})

# 绘制图片
    g = (
        Graph(
            init_opts=opts.InitOpts(width="1500px", height="800px")
        )
        .add("", nodes, links,
             # 是否开启鼠标缩放和平移漫游。
             is_roam=True,
             # 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。
             is_focusnode=True,
             # 节点之间的斥力因子。
             # 支持设置成数组表达斥力的范围，此时不同大小的值会线性映射到不同的斥力。值越大则斥力越大
             repulsion=5000,
             # 标签配置项，参考 `series_options.LabelOpts`
             label_opts=opts.LabelOpts(is_show=True),
             # layout='circular',
             # 关系边的公用线条样式。
             linestyle_opts=opts.LineStyleOpts(width=1, curve=0.1, opacity=0.5),
                )
            .set_global_opts(title_opts=opts.TitleOpts(title="金庸小说人物关系"))
    )
    g.render("graph_jinyong_novels.html")

if __name__ == '__main__':
    drawing_graph()