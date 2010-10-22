import os

from scrapy.conf import settings
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from tw_image.items import TwImageItem

class TwImageSpider(BaseSpider):
  name = 'maitreya'
  allowed_domains = ['maitreya.org.tw']

  def __init__(self):
    path = os.path.join(os.getcwd(), settings['URL_LIST_PATH'])
    if os.path.exists(path):
      f = open(path, 'r')
      self.start_urls = [url.rstrip() for url in f.readlines()]

  def parse(self, response):
    hxs = HtmlXPathSelector(response)
    item = TwImageItem()
    item['image_urls'] = hxs.select("//a[contains(@rel, 'image_group')]/@href").extract()
    if not item['image_urls']:
      item['image_urls'] = hxs.select("//a[contains(@rel, 'lightbox')]/@href").extract()
    return item

SPIDER = TwImageSpider()
