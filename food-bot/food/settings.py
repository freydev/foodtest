# Scrapy settings for products project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import os
import sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(BASEDIR, 'findfood'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'findfood.settings'

BOT_NAME = 'food'

SPIDER_MODULES = ['food.spiders']
NEWSPIDER_MODULE = 'food.spiders'
LOG_LEVEL = 'INFO'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'products (+http://www.yourdomain.com)'
ITEM_PIPELINES = {
    'food.pipelines.ProductsPipeline': 100,
    'food.pipelines.RecipesPipeline': 200,
}