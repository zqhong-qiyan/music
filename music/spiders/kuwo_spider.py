# -*- coding:utf-8 -*-
"""
@author:zhouqiuhong
@file:kuwo_spider.py
@time:2018/12/10 001010:18
"""
import scrapy
from scrapy.loader import ItemLoader
from scrapy.http import Request
from music.items import MusicItem


class KuwoSpider(scrapy.Spider):
    name = "kuwo"
    allowed_domain = "www.kuwo.cn"
    start_urls = ["http://www.kuwo.cn/playlist/index?pid=1082685104"]

    def parse(self, response):
        item_loader = ItemLoader(item=MusicItem(), response=response)
        item_loader.add_xpath("url", "//ul[@class='listMusic']//div[@class='name']/a/@href")
        item_loader.add_xpath("name", "//ul[@class='listMusic']//div[@class='name']/a/text()")
        print(item_loader.load_item())
        # res_text = response.text
        # url = response.xpath("//ul[@class='listMusic']//div[@class='name']/a/@href").extract()
        # name = response.xpath("//ul[@class='listMusic']//div[@class='name']/a/text()").extract()
        # print(name, ": ", url)
