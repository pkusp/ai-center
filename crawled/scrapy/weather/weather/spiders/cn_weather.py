# -*- coding: utf-8 -*-
import scrapy


class CnWeatherSpider(scrapy.Spider):
    name = 'cn_weather'
    allowed_domains = ['www.nmc.cn/']
    start_urls = ['http://www.nmc.cn//']

    def parse(self, response):
        pass
