# -*- coding: utf-8 -*-
# @Time : 2020/12/22 17:35
# @Author : tanyao1345@163.com
# @FileName: relationships_graph.py
# @Software: PyCharm
# @desc:
import pandas as pd
from pyecharts.charts import Graph
from pyecharts import options as opts


def drawing_graph():
    node_data = pd.read_csv("./library_joy_of_life/qyn_role.csv")
    relationship_data = pd.read_csv("./library_joy_of_life/qyn_relationship.csv")

    node_data_list = node_data.values.tolist()
    relationship_data_list = relationship_data.values.tolist()

    nodes = []
    for node in node_data_list:
        # 范闲陈萍萍出场次数过多，平衡一下图像大小
        if node[0] == "范闲":
            node[2] = node[2] / 10
        if node[0] == "陈萍萍":
            node[2] = node[2] / 2
        nodes.append({"name": node[0], "symbolSize": node[2] / 30})
        # nodes.append({'name': node[0], 'symbolSize': node[1]})

    links = []
    for link in relationship_data_list:
        links.append({'source': link[0], 'target': link[1], 'value': link[2]})

    # 绘制图片
    g = (
        Graph(
            init_opts=opts.InitOpts(width="1800px", height="900px")
        )
        .add("", nodes, links,
             # 是否开启鼠标缩放和平移漫游。
             is_roam=True,
             # 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。
             is_focusnode=True,
             # 节点之间的斥力因子。
             # 支持设置成数组表达斥力的范围，此时不同大小的值会线性映射到不同的斥力。值越大则斥力越大
             repulsion=10000,
             # 标签配置项，参考 `series_options.LabelOpts`
             label_opts=opts.LabelOpts(is_show=True),
             # 关系边的公用线条样式。
             linestyle_opts=opts.LineStyleOpts(width=1, curve=0.1, opacity=0.5),
                )
            .set_global_opts(title_opts=opts.TitleOpts(title="庆余年人物关系"))
    )
    g.render("graph_joy_of_life.html")

if __name__ == '__main__':
    drawing_graph()

