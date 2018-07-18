# -*- coding: utf-8 -*-
import scrapy
from weather.items import MovieItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://meijutt.com/']

    def parse(self, response):
        print('\n\n\n',response.xpath(),'\n\n\n------------')
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for each_movie in movies:
            print('______each_______')
            item = MovieItem()
            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
            yield item
