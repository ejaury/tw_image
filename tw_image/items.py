# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class TwImageItem(Item):
    # define the fields for your item here like:
    # name = Field()
    image_urls = Field()
    image_paths = Field()
