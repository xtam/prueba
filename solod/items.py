# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class SolodItem(Item):
    # define the fields for your item here like:
    # name = Field()
    name = Field()
    ip = Field()
    address = Field()
    phone = Field()
    web = Field()
    original_name = Field()
    numid = Field()
