# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import hashlib
import pymongo
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class MongoPipelineTayara:
    COLLECTION_NAME = "tayara"

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE"),
        )
    
    # opens a connection to mongodb when the spider starts
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if spider.name != "tayara":
            return None
        # core functionnalities (clean, insert ..)
        item_id = self.compute_item_id(item)
        if self.db[self.COLLECTION_NAME].find_one({"_id": item_id}):
            raise DropItem(f"Duplicate item found: {item}")
        else:
            item["_id"] = item_id
            self.db[self.COLLECTION_NAME].insert_one(ItemAdapter(item).asdict())
            return item

    def compute_item_id(self, item):
        unique_data = (
            str(item.get("gouvernorat", "")) +
            str(item.get("delegation", "")) +
            str(item.get("prix", "")) +
            str(item.get("superficie", "")) +
            str(item.get("salle_de_bains", "")) +
            str(item.get("chambres", "")) +
            str(item.get("description", ""))
        )
        return hashlib.sha256(unique_data.encode()).hexdigest()


class MongoPipelineMubawab:
    COLLECTION_NAME = "mubawab"

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE"),
        )
    
    # opens a connection to mongodb when the spider starts
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if spider.name != "mubawab":
            return None
        # core functionnalities (clean, insert ..)
        item_id = self.compute_item_id(item)
        if self.db[self.COLLECTION_NAME].find_one({"_id": item_id}):
            raise DropItem(f"Duplicate item found: {item}")
        else:
            item["_id"] = item_id
            self.db[self.COLLECTION_NAME].insert_one(ItemAdapter(item).asdict())
            return item

    def compute_item_id(self, item):
        unique_data = (
            str(item.get("gouvernorat", "")) +
            str(item.get("delegation", "")) +
            str(item.get("prix", "")) +
            str(item.get("superficie", "")) +
            str(item.get("salle_de_bains", "")) +
            str(item.get("chambres", "")) +
            str(item.get("description", ""))
        )
        return hashlib.sha256(unique_data.encode()).hexdigest()
