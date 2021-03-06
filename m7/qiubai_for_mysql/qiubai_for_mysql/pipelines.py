# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import redis

class TxtPipeline(object):
    def open_spider(self,spider):
        self.f = open('qiubai.txt', 'a' , encoding='utf-8')

    def process_item(self, item, spider):
        author = item['author']
        duanzi = item['duanzi']

        self.f.write(author+':'+duanzi+'\n\n\n')

        return item

    def close_spider(self,spider):
        self.f.close()

class MysqlTestPipeline(object):
    def open_spider(self,spider):
        self.conn = pymysql.connect(
            host='140.143.132.118',
            port=3306,
            user='xiaoxin',
            password='Nishi458_2',
            db='qiubai',
            charset='utf8'
        )
        self.sql = 'insert into qiushi(author, content) values(%s,%s)'
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        print(item)
        author = item['author']
        duanzi = item['duanzi']

        try:
            self.cursor.execute(self.sql,(author,duanzi))
            self.conn.commit()
        except Exception:
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

class RedisPipeline(object):

    def open_spider(self, spider):
        self.conn = redis.Redis(
            host='127.0.0.1',
            port=6379,
            charset='utf8'
        )

    def process_item(self, item, spider):
        author = item['author']
        duanzi = item['duanzi']

        qiushi = {
            'author': author,
            'duanzi': duanzi
        }

        self.conn.lpush('qiubai', str(qiushi))

        return item
