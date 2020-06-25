# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class DoubanPipeline(object):
    # print("#"*50)
    def __init__(self):
        # print("#"*50)
        f=open('douban_drama.csv','w',newline='',encoding='utf-8')
        fieldnames=[
            'title','url','rate'
        ]
        self.writer = csv.DictWriter(f, fieldnames=fieldnames)
        self.writer.writeheader()
        
    def process_item(self, item, spider):
        
        self.writer.writerow(item)
        return item
