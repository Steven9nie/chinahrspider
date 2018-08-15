# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinahrItem(scrapy.Item):

    jobName = scrapy.Field()
    salary = scrapy.Field()
    jobDistrict = scrapy.Field()
    jobProperty = scrapy.Field()
    educat = scrapy.Field()
    jobExp =scrapy.Field()
    welfare = scrapy.Field()

    companyName = scrapy.Field()
    industry = scrapy.Field()
    companyScale = scrapy.Field()
    companyProperty = scrapy.Field()

    ability = scrapy.Field()

