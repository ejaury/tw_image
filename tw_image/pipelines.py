# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import os
import urllib2

from scrapy.conf import settings

class TwImagePipeline(object):
    def process_item(self, spider, item):
      current_path = ''
      for url in item['image_urls']:
        result = urllib2.urlopen(url)
        dirname = url.split('/')[-2]
        full_dirname = os.path.join(settings.get('IMAGES_STORE'),
                                    dirname)
        if not os.path.exists(full_dirname):
          os.makedirs(full_dirname)
        current_path = full_dirname
        path = os.path.join(full_dirname, os.path.basename(url))
        f = open(path, 'w')
        f.write(result.read())
        f.close()
      print current_path
      return item
