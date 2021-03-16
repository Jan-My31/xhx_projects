# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# class TbCrawlItem(DjangoItem):
#     django_model = Infolist



class TbCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id =scrapy.Field()
    info_text =scrapy.Field()
    info_id =scrapy.Field()
    info_type = scrapy.Field()
    info_market = scrapy.Field()
    info_date =scrapy.Field()
    # 公告链接
    info_link=scrapy.Field()
    info_detail=scrapy.Field()
    update_time=scrapy.Field()
    create_time=scrapy.Field()

