from scrapy.spiders import CrawlSpider, Rule
from wikiSpider.items import Article
from scrapy.linkextractors import LinkExtractor

class ArticleSpider(CrawlSpider): #
    
    name = "article" #spider name
    allowed_domains = ["en.wikipedia.org"]#only follow links from this domain
    start_urls = ["http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
    rules = [ 
        Rule(LinkExtractor(allow=('(/wiki/)((?!:).)*$'),), callback="parse_item", follow=True)
    ]

    custom_settings = {
        'DEPTH_LIMIT': 1,
        'DOWNLOAD_DELAY' : 0.25
    }

    def parse_item(self, response):
        item = Article() 
        title = response.css('#firstHeading::text').extract_first()
        content =  response.css('#toc *::text').extract()
        print("Title is: "+title)
        item['title'] = title
        item['content'] = content
        return item