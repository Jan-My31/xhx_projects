# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi
from redis import Redis


class TbCrawlPipeline(object):
    conn = None

    def open_spider(self, spider):
        self.conn = spider.conn

    def process_item(self, item, spider):
        dic = {
            'info_text': item['info_text'],
            'info_id': item['info_id'],
            'info_type': item['info_type'],
            'info_market': item['info_market'],
            'info_date': item['info_date'],
            'info_link': item['info_link'],
            # 'info_detail': item['info_detail']
        }
        self.conn.lpush('info_list', dic)
        return item


class TbCrawl_MysqlPipeline(object):
    def __init__(self, host, user, password, db):
        params = dict(
            host=host,
            user=user,
            password=password,
            db=db,
            charset='utf8',  # 不能用utf-8
            cursorclass=pymysql.cursors.DictCursor
        )
        # 使用Twisted中的adbapi获取数据库连接池对象
        self.dbpool = adbapi.ConnectionPool('pymysql', **params)

    @classmethod
    def from_crawler(cls, crawler):
        # 获取settings文件中的配置
        host = crawler.settings.get('HOST')
        user = crawler.settings.get('USER')
        password = crawler.settings.get('PASSWORD')
        db = crawler.settings.get('DB')
        return cls(host, user, password, db)

    def process_item(self, item, spider):
        # 使用数据库连接池对象进行数据库操作,自动传递cursor对象到第一个参数
        query = self.dbpool.runInteraction(self.do_insert, item)
        # 设置出错时的回调方法,自动传递出错消息对象failure到第一个参数
        query.addErrback(self.on_error, spider)
        return item

        # 插入数据

    def do_insert(self, cursor, item):
        # sql = 'INSERT INTO bitauto_list(bbs_name,posts,posts_url,reply,page_view,posted_name,posted_time,content)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        # sql = 'INSERT INTO tb_web_infolist(id,info_text, info_id,info_type, info_market, info_date, info_link )VALUES(%s,%s,%s,%s,%s,%s,%s)'
        sql = 'INSERT INTO infos_list(id,info_text, info_id,info_type, info_market, info_date, info_link,info_detail,update_time,create_time)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        #
        args = (

            item['id'],
            item['info_text'],
            item['info_id'],
            item['info_type'],
            item['info_market'],
            item['info_date'],
            item['info_link'],
            item['info_detail'],
            item['update_time'],
            item['create_time'],

        )
        cursor.execute(sql, args)

    def on_error(self, failure, spider):
        spider.logger.error(failure)
