# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline


class ScrapyspiderPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        file_name: str = request.url
        return file_name
