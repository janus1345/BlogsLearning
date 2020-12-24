# -*- coding: utf-8 -*-
# @Time : 2020/12/24 17:16
# @FileName: crawler_jinyong_novels.py
# @Software: PyCharm
# @desc:
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


class PaChong:
    def __int__(self, URL, URL_ID, URL_Base):
        self.URL = URL
        self.URL_ID = URL_ID
        self.URL_Base = URL_Base
        self.listpath = None

    def OpenSeeion(self):
        """
        获取小说所有章节连接
        :return:
        """
        try:
            response = urlopen(self.URL)
            html = response.read()
            soup = BeautifulSoup(html)
            OringialPath = soup.find_all(class_="mlist")
            #
            pattern = re.compile('(?<=href=").*?(?=")')
            print("pattern", pattern)
            print("OringialPath", OringialPath)
            self.listpath = re.findall(pattern, str(OringialPath))
        except:
            print("error")




if __name__ == '__main__':
    URL = list()
    URL.append("http://www.jinyongwang.com/fei/")  # 飞狐外传
    # URL.append("http://www.jinyongwang.com/xue/")  # 雪山飞狐
    # URL.append("http://www.jinyongwang.com/lian/")  # 连城诀
    # URL.append("http://www.jinyongwang.com/tian/")  # 天龙八部
    # URL.append("http://www.jinyongwang.com/she/")  # 射雕英雄传
    # URL.append("http://www.jinyongwang.com/bai/")  # 射雕英雄传
    # URL.append("http://www.jinyongwang.com/lu/")  # 射雕英雄传
    # URL.append("http://www.jinyongwang.com/xiao/")  # 射雕英雄传
    # URL.append("http://www.jinyongwang.com/shu/")  # 射雕英雄传
    # URL.append("http://www.jinyongwang.com/shen/")  # 射雕英雄传
    # URL.append("http://www.jinyongwang.com/xia/")  # 射雕英雄传
    # URL.append("http://www.jinyongwang.com/yi/")  # 射雕英雄传
    # URL.append("http://www.jinyongwang.com/bi/")  # 射雕英雄传
    # URL.append("http://www.jinyongwang.com/yuan/")  # 射雕英雄传
    # URL.append("http://www.jinyongwang.com/yue/")  # 射雕英雄传

    response = urlopen("http://www.jinyongwang.com/fei/")
    html = response.read()
    soup = BeautifulSoup(html)
    OringialPath = soup.find_all(class_="mlist")
    pattern = re.compile('(?<=href=").*?(?=")')
    listpath = re.findall(pattern, str(OringialPath))
    print("pattern", pattern)
    print("OringialPath", OringialPath)
    print("listpath", listpath)