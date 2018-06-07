# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import pymysql


class CarHomePipeline(object):
    def process_item(self, item, spider):
        return item


class CarHome_INFO_Pipeline(object):
    def __init__(self):
        self.file = codecs.open("car.json", "w", encoding='utf-8')


    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item

    def close_spider(self, spider):
        self.file.close()


class CarHomeSQLPipeline(object):
    def __init__(self):
        # 刚开始时连接数据库
        self.connect = pymysql.connect(host='127.0.0.1', user='root', passwd='root',
                                       db='car_home', charset='utf8', use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

        try:
            # 插入数据
            self.cursor.execute(
                """insert into info(Car_Name, Car_Class, Car_url, New_car_guide ,Car_Engine, Speed_Changing_Box, Body_structure, Car_Color)
                value (%s, %s, %s, %s, %s, %s, %s, %s)""",
                (item['Car_Name'],
                 item['Car_Class'],
                 item['Car_url'],
                 item['New_car_guide'],
                 item['Engine'],
                 item['Speed_Changing_Box'],
                 item['Body_structure'],
                 item['Car_Color']
            ))

            # 提交sql语句
            self.connect.commit()

        except Exception as error:
            # 出现错误时打印错误日志
            log(error)
            self.connect.commit()
        return item

    def close_spider(self, spider):
        self.connect.close()