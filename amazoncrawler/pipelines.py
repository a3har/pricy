# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter, CsvItemExporter
import os


class AmazoncrawlerPipeline:
    def process_item(self, item, spider):
        return item


class JsonPipeline(object):
    def __init__(self):
        filename = "data/phones.json"
        os.makedirs('data', exist_ok=True)
        self.file = open(filename, 'wb')
        self.exporter = JsonItemExporter(
            self.file, encoding='utf-8', ensure_ascii=False, indent=4)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class CsvPipeline(object):
    def __init__(self):
        filename = "data/phones.csv"
        os.makedirs('data', exist_ok=True)
        self.file = open(filename, 'wb')
        self.exporter = CsvItemExporter(self.file, include_headers_line=True)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        # self.create_valid_csv(item)
        self.exporter.export_item(item)
        return item

    def create_valid_csv(self, item):
        for key, value in item.items():
            is_string = (isinstance(value, str))
            if (is_string and ("," in value.encode('utf-8'))):
                item[key] = "\"" + value + "\""
