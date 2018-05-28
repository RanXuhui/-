# -*- coding: utf-8 -*-
import scrapy


class AutoSpiderSpider(scrapy.Spider):
    name = 'auto_spider'
    allowed_domains = ['autohome.com.cn']
    start_urls = ['http://autohome.com.cn/']

    def start_requests(self):
        reqs = []

        # req = scrapy.Request("http://www.xicidaili.com/nn/%s"%i)
        req = scrapy.Request("https://www.autohome.com.cn/beijing/")
        reqs.append(req)
        return reqs

    def parse(self, response):
        Car_Calss_Web = response.xpath('//div[@class="homepage-hotcar"]')  # 选取所有所有div元素，且这些元素拥有值为homepage-hotcar的class属性

        trs = ip_list[0].xpath('tr')

        items = []
