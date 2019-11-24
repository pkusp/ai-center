# -*- coding: utf-8 -*-
import scrapy
import os
from weather.items import PicItem

class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['xiaohua.com']
    start_urls = ['http://xiaohua.com/']

    def parse(self, response):
                # 获取所有图片的a标签
        allPics = response.xpath('//div[@class="img"]/a')
        for pic in allPics:
            # 分别处理每个图片，取出名称及地址
            item = PicItem()
            name = pic.xpath('./img/@alt').extract()[0]
            addr = pic.xpath('./img/@src').extract()[0]
            addr = 'http://www.xiaohuar.com'+addr
            item['name'] = name
            item['addr'] = addr
            # 返回爬取到的数据
            yield item
