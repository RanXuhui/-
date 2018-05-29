# -*- coding: utf-8 -*-
import scrapy
from car_home.items import CarHomeItem


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

        Car_Name = Car_Calss_Web.xpath('div/div/ul/li/div[@class="box"]/p[@data-gcjid]')

        items = []

        for Car_Class in Car_Top:
            pre_item = CarHomeItem()
            pre_item['Car_Class'] = Car_Class.xpath('string(a)').extract()
            items.append(pre_item)
            for Car in Car_Name:
                pre_item = CarHomeItem()
                pre_item['Car_Name'] = Car.xpath('string(a)').extract()[0]
                items.append(pre_item)

        return items
