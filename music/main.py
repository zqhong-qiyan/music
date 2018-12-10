# -*- coding:utf-8 -*-
"""
@author:zhouqiuhong
@file:main.py
@time:2018/12/10 001010:19
"""
from scrapy.cmdline import execute

if __name__ == "__main__":
    execute(["scrapy", "crawl", "kuwo"])