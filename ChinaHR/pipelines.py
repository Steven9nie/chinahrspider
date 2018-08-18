# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql


class ChinahrPipeline(object):
    """清洗后的数据入库"""
    def __init__(self):
        # 连接数据库
        self.conn = None
        # 游标
        self.cur = None

    def open_spider(self, spider):
        self.conn = pymysql.connect(host='127.0.0.1',
                                    user='root',
                                    password="123456",
                                    database='chinahr',
                                    port=3306,
                                    charset='utf8')

        self.cur = self.conn.cursor()

    def process_item(self, item, spider):

        fields, values = zip(*item.items())
        sql = "INSERT INTO `%s`(%s) VALUES (%s)" % (
            'jobs',
            ','.join(fields),
            ','.join(["%s"] * len(values))
        )
        print(sql, values)

        self.cur.execute(sql, values)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
