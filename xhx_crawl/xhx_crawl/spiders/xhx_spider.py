# -*- coding: utf-8 -*-
import scrapy
import copy ,uuid,datetime,time
from xhx_crawl.items import XhxCrawlItem
from redis import Redis

class XhxSpiderSpider(scrapy.Spider):
    name = 'xhx_spider'
    # allowed_domains = ['95306.cn']
    start_urls = [
        #
        # 'http://wz.beij.95306.cn/mainPageNoticeList.do?method=init&id=5000001&cur=1',
        # 'http://wz.taiy.95306.cn/mainPageNoticeList.do?method=init&id=5000001&cur=1',
        # 'http://wz.huhht.95306.cn/mainPageNoticeList.do?method=init&id=5000001&cur=1',
        # 'http://www.ztwz.com/mainPageNoticeList.do?method=init&id=5000001&cur=1',
        # 'http://wz.zhengzh.95306.cn/mainPageNoticeList.do?method=init&id=5000001&cur=1',
        # 'http://wz.wuh.95306.cn:7001/mainPageNoticeList.do?method=init&id=5000001&cur=1',
        # 'http://wz.xian.95306.cn/mainPageNoticeList.do?method=init&id=5000001&cur=1',
        # 'http://wz.jin.95306.cn:7001/mainPageNoticeList.do?method=init&id=5000001&cur=1',
        # 'http://wz.shangh.95306.cn/mainPageNoticeList.do?method=init&id=5000001&cur=1',
        # 'http://wz.nanch.95306.cn/mainPageNoticeList.do?method=init&id=5000001&cur=1',
        # 'http://wz.guangzh.95306.cn/mainPageNoticeList.do?method=init&id=5000001&cur=1',
        # 'http://wz.nann.95306.cn/mainPageNoticeList.do?method=init&id=5000001&cur=1',
        # 'http://wz.chengd.95306.cn/mainPageNoticeList.do?method=init&id=5000001&cur=1',
        # 'http://wz.kunm.95306.cn/mainPageNoticeList.do?method=init&id=5000001&cur=1',
        # 'http://wz.lanzh.95306.cn/mainPageNoticeList.do?method=init&id=5000001&cur=1',
        # 'http://wz.wulmq.95306.cn/mainPageNoticeList.do?method=init&id=5000001&cur=1',
        # 'http://wz.qingz.95306.cn/mainPageNoticeList.do?method=init&id=5000001&cur=1',
        # 'http://wz.th.95306.cn/mainPageNoticeList.do?method=init&id=5000001&cur=1',
        # 'http://wz.jzx.95306.cn/mainPageNoticeList.do?method=init&id=5000001&cur=1',
        'http://wz.sheny.95306.cn/mainPageNoticeList.do?method=init&id=5000001&cur=1'
    ]
    conn = Redis(host='45.15.10.32', encoding='utf-8', port=6388, password='Xhx121314.')
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'Cookie': 'JSESSIONID=-CG4KEsakDs23cRypz7xdDSGmwRDvhY_yS-g54FM7Se2IQupqNnC!-1236011016'
        }

        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse, dont_filter=True,
                                 meta={'url': copy.deepcopy(url)})

    def parse(self, response):
        if response.status == 200:
            # print(response.text)
            url = response.meta['url']
            # print(url)
            try:
                list_info = response.xpath('//table[@class="listInfoTable"]//tr')
                for info in list_info:
                    if info != []:
                        info_text = info.xpath('normalize-space(./td[1]/a/text())').extract_first()
                        info_id = info.xpath('normalize-space(./td[2]/text())').extract_first()
                        info_type = info.xpath('normalize-space(./td[3]/text())').extract_first()
                        info_market = info.xpath('normalize-space(./td[4]/text())').extract_first()
                        info_date = info.xpath('normalize-space(./td[5]/text())').extract_first()
                        # 公告链接
                        if info.xpath('./td[1]/a/@href'):
                            info_link = url[:-50] + info.xpath('./td[1]/a/@href')[0].extract()

                            item = XhxCrawlItem()
                            item['id'] = str(uuid.uuid1()).replace("-", '')
                            item['info_text'] = info_text
                            item['info_id'] = info_id
                            item['info_type'] = info_type
                            item['info_market'] = info_market
                            item['info_date'] = info_date
                            item['info_link'] = info_link
                            item['update_time'] = info_date
                            item['create_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

                            ex=self.conn.sadd('info_link',info_link)

                            if ex==1:

                                print("该url没有被爬取过,可以进行数据爬取")
                            # yield item
                                yield scrapy.Request(url=info_link, callback=self.detail_parse,
                                                 meta={'item': copy.deepcopy(item)}, dont_filter=True)
                            else:
                                print("数据没有进行更新，没有数据抓取")

            except Exception as ex:
                print(ex)

    def detail_parse(self, response):
        print(response.text)
        try:
            item = response.meta['item']

            info_detail = response.xpath('//div[@class="registerRegionFrameMid"]').extract_first()
            # info_style=response.xpath('//div[@class="registerRegionFrameMid"]/div[@class="noticeBox"]/div[@class="divAbs"]/style/text()').extract_first()

            # info_detail=info_detail.replace(info_style,'').replace('startprint','')
            item['info_detail'] = info_detail
            yield item



        except Exception as e:
            print(e)

