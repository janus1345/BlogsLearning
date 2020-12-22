import random

from pyecharts.charts import Graph
from pyecharts.render import make_snapshot
from pyecharts import options as opts
import pandas as pd

def deal_graph():
    edge_data = pd.read_csv('qyn_edge.csv')
    node_data = pd.read_csv('qyn_node.csv')

    edge_data_list = edge_data.values.tolist()
    node_data_list = node_data.values.tolist()

    nodes = []
    for node in node_data_list:
        # 范闲陈萍萍出场次数过多，平衡一下图像大小
        if node[0] == "范闲":
            node[2] = node[2]/10
        if node[0] == "陈萍萍":
            node[2] = node[2]/2
        nodes.append({"name": node[0], "symbolSize": node[2]/30})

    links = []

    for link in edge_data_list:
        links.append({"source": link[0], "target": link[1], "value": link[2]})

    rgb = lambda: random.randint(0,255)
    
    # 绘制图形
    g = (
        Graph(init_opts=opts.InitOpts(width="1800px", height="900px"))
        .add("", nodes, links, 
            is_roam=True,
            is_focusnode=True,
            #itemstyle_opts=opts.ItemStyleOpts(color=color),
            label_opts=opts.LabelOpts(is_show=True),
            # layout='circular',
            linestyle_opts=opts.LineStyleOpts(width=1, curve=0.1, opacity=0.5),
            repulsion=10000
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="庆余年人物关系"))
    )
    g.render()

deal_graph()