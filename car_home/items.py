# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarHomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Car_Class = scrapy.Field()
    Car_Name = scrapy.Field()
    Car_url = scrapy.Field()
    New_car_guide = scrapy.Field()
    # Mall_price = scrapy.Field()
    # Secondhand_price = scrapy.Field()
    Engine = scrapy.Field()
    Speed_Changing_Box = scrapy.Field()
    Speed_Changing_Box_2 = scrapy.Field()
    Body_structure = scrapy.Field()
    Car_Color = scrapy.Field()
