from scrapy import Item, Field

class Article(Item):
    # define the fields for your item here like
    title = Field()
    content = Field()