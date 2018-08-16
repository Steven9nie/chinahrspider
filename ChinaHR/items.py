# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinahrItem(scrapy.Item):
    """定义抽取的信息字段"""

    jobName = scrapy.Field()  # 职位名
    salary = scrapy.Field()  # 职位薪资
    jobDistrict = scrapy.Field()  # 职位所属地区
    jobProperty = scrapy.Field()  # 职位性质
    educat = scrapy.Field()  # 学历要求
    jobExp =scrapy.Field()  # 就业经验要求
    welfare = scrapy.Field()  # 职位福利

    companyName = scrapy.Field()  # 招聘企业名
    industry = scrapy.Field()  # 企业所属行业
    companyScale = scrapy.Field()  # 企业规模
    companyProperty = scrapy.Field()  # 企业性质

    ability = scrapy.Field()  # 岗位要求说明

