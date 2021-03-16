# -*- coding: utf-8 -*-

# Scrapy settings for tb_crawl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import sys
import os
import scrapy_redis
# from django.core.wsgi import get_wsgi_application
#
# DJANGO_PROJECT_PATH="apps"
# DJANGO_SETTINGS_MODULE="apps.settings"

# sys.path.append(os.path.dirname(os.path.abspath('.')))
# os.environ['DJANGO_SETTINGS_MODULE'] = 'apps.settings'
# import django
# django.setup()




BOT_NAME = 'tb_crawl'

SPIDER_MODULES = ['tb_crawl.spiders']
NEWSPIDER_MODULE = 'tb_crawl.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tb_crawl (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tb_crawl.middlewares.TbCrawlSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'tb_crawl.middlewares.TbCrawlDownloaderMiddleware': 543,
    # 'tb_crawl.middlewares.RandomUserAgentMiddlware': 543,
    # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}

#随机usergent
RANDOM_UA_TYPE = 'random'
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'tb_crawl.pipelines.TbCrawlPipeline': 300,
    'tb_crawl.pipelines.TbCrawl_MysqlPipeline':100,
    'scrapy_redis.pipelines.RedisPipeline': 100,
}
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
#
# #去重容器,Redis的set集合来存储请求的指纹数据, 从而实现请求去重的持久化
# DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
# #增加了调度的配置, 作用: 把请求对象存储到Redis数据, 从而实现请求的持久化.
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
# #配置调度器持久化
SCHEDULER_PERSIST = True
# 确保所有的爬虫实例使用Redis进行重复过滤
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"


# Requests的调度策略，默认优先级队列
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'


# #redis_url 配置
REDIS_HOST = ''
REDIS_PORT = 6388
REDIS_PARAMS = {'password': '',}


#调度配置 请求对象存储到Redis数据

# Mysql数据库参数
HOST = ''
USER = 'xhx'
PASSWORD = '.'
DB ='xhx_projects'

#日志存储
EED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL= 'DEBUG'

#出现状态码之再次访问
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 408]
RETRY_TIMES = 1

HTTPERROR_ALLOWED_CODES = [418]