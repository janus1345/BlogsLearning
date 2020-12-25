# -*- coding: utf-8 -*-
# @Time : 2020/12/24 17:16
# @FileName: crawler_jinyong_novels.py
# @Software: PyCharm
# @desc:
import re
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import codecs


def OpenSeeion(URL):
    """
    获取小说所有章节连接
    :return: 返回所有的章节连接列表 和 小说标题
    """
    try:
        response = urlopen(URL)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        # 获取小说的标题
        title = soup.find(class_="title").span.text
        OringialPath = soup.find_all(class_="mlist")
        pattern = re.compile('(?<=href=").*?(?=")')
        listpath = re.findall(pattern, str(OringialPath))
        return listpath, title
    except Exception as e:
        print("error", e)


def gettext(section_url):
    """
    获取该章节所有段落，返回数据类型是list
    :param sessionURL: 获取到到小说章节连接
    :return:
    """
    content = []
    for url in section_url:
        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        title = soup.find(id="title").text
        pattern = re.compile('(?<=<p>).*?(?=</p>)')
        text = re.findall(pattern, str(soup))
        content.append("{}\r\n".format(title))
        content.extend(text)
        time.sleep(5)
    return content


def save_novels(text, title):
    """
    存入小说
    :param text:
    :return:
    """
    try:
        with codecs.open("./jinyong_novels_library/{}.txt".format(title), "a+", "utf-8") as f:
            f.writelines(text)
        print("保存成功")
    except Exception as e:
        print("错误", e)


if __name__ == '__main__':
    URL = list()
    URL.append("http://www.jinyongwang.com/fei/")  # 飞狐外传
    URL.append("http://www.jinyongwang.com/xue/")  # 雪山飞狐
    URL.append("http://www.jinyongwang.com/lian/")  # 连城诀
    URL.append("http://www.jinyongwang.com/tian/")  # 天龙八部
    URL.append("http://www.jinyongwang.com/she/")  # 射雕英雄传
    URL.append("http://www.jinyongwang.com/bai/")  # 白马啸西风
    URL.append("http://www.jinyongwang.com/lu/")  # 鹿鼎记
    URL.append("http://www.jinyongwang.com/xiao/")  # 笑傲江湖
    URL.append("http://www.jinyongwang.com/shu/")  # 书剑恩仇录
    URL.append("http://www.jinyongwang.com/shen/")  # 神雕侠侣
    URL.append("http://www.jinyongwang.com/xia/")  # 侠客行
    URL.append("http://www.jinyongwang.com/yi/")  # 倚天屠龙记
    URL.append("http://www.jinyongwang.com/bi/")  # 碧血剑
    URL.append("http://www.jinyongwang.com/yuan/")  # 鸳鸯刀
    URL.append("http://www.jinyongwang.com/yue/")  # 越女剑
    for url in URL:
        listpath, title = OpenSeeion(url)
        listpath = ["http://www.jinyongwang.com" + path for path in listpath]
        print("list", listpath)
        content = gettext(listpath)
        text = "\r\n\n".join(content)
        save_novels(text, title)