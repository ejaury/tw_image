# Scrapy settings for tw_image project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
# Or you can copy and paste them from where they're defined in Scrapy:
# 
#     scrapy/conf/default_settings.py
#

BOT_NAME = 'tw_image'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['tw_image.spiders']
NEWSPIDER_MODULE = 'tw_image.spiders'
DEFAULT_ITEM_CLASS = 'tw_image.items.TwImageItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

URL_LIST_PATH = 'tw_image/urls.lst'
ITEM_PIPELINES = ['tw_image.pipelines.TwImagePipeline']
IMAGES_STORE = '/home/edwin/temple_website/downloaded_omei_imgs'
