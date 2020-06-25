&ensp;&ensp;通过分析数据接口爬取豆瓣中评分9分以上的美剧的名字，评分，详情链接。并保存在文件'douban_drama.csv'中.✔

# 爬取
进入有pipfile的那个文件的目录在pipenv shell 之后输入：
```batch
scrapy crawl drama
```
开始爬虫
然后就可以在当前目录下看到的数据爬取保存在了'douban_drama.csv'文件下了。
