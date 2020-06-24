# -*- coding: utf-8 -*-
import scrapy
import json
from douban.items import DoubanItem

def debug(a):
    print("###{}###".format(a))

class DramaSpider(scrapy.Spider):
    name = 'drama'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start=0']
    start=0

    def parse(self, response):
        data=json.loads(response.text)
        for subject in data['subjects']:
            if subject['rate']<'9':
                continue

            info_item=DoubanItem()
            info_item['title']=subject['title']
            info_item['rate']=subject['rate']
            info_item['url']=subject['url']
            yield info_item
        self.start+=20
        # debug(self.start)
        next_url='https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start={}'.format(self.start)

        yield scrapy.Request(next_url,callback=self.parse)
