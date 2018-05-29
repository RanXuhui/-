# -*- coding: utf-8 -*-
import scrapy
from car_home.items import CarHomeItem
import re

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
        Car_Calss_Web = response.xpath('//div[@class="list"]')  # 选取所有所有div元素，且这些元素拥有值为homepage-hotcar的class属性

        Car_Top = Car_Calss_Web.xpath('div[@class="name"]')

        Car_Name = Car_Calss_Web.xpath('div[2]/div/ul/li/div/p[@data-gcjid]')

        Car_url = Car_Calss_Web.xpath('div[2]/div/div/ul/li/div/p')

        items = []

        for Car_Class in Car_Top:
            pre_item = CarHomeItem()
            pre_item['Car_Class'] = Car_Class.xpath('string(a)').extract()
            items.append(pre_item)
            for Car in Car_Name:
                pre_item = CarHomeItem()
                pre_item['Car_Name'] = Car.xpath('string(a)').extract()[0]

                pre_item['Car_url_1'] = Car.xpath('a').re('\/\d+\/')
                pre_item['Car_url_2'] = Car.xpath('a').re('=\d+')
                items.append((pre_item))
        return items
        # yield scrapy.Request(Car_Name_index=item['Car_Name'], meta={'item':item}, callback=self.parse_detail)

    # def pares_detail(self, response):

        # div = response.xpath('//div[@class="hotcar-content"]/div[@id="hotcar-1"]/div/div[2]/div/ul/li[1]/div/p[1]')