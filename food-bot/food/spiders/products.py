# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from food.items import ProductsItem


class ProductsSpider(CrawlSpider): # findfood
    name = 'products'
    allowed_domains = ['findfood.ru']
    start_urls = ['http://findfood.ru/product']

    rules = (
            Rule(SgmlLinkExtractor(allow=r'product/[\S]+', deny=(r'\?', 'index', 'login')), follow=False, callback='parse_item'),
            Rule(SgmlLinkExtractor(allow=r'product/.+?Product_page[\S]+'), follow=True),
        )

    def parse_item(self,response):
    	# ахтунг! костыль, почему то проходит url "http://findfood.ru/site/login"
    	if 'product' in response.url:
	        sel = Selector(response)
	        title = sel.xpath('//*[@id="page"]/div[3]/div/span/text()').extract() or [None]
	        category = sel.xpath('//*[@id="page"]/div[3]/div/a[3]/text()').extract() or [None]
	        src = sel.xpath('//*[@id="bigphoto"]/img/@src').extract() or [None]
	        image = 'http://findfood.ru/%s' %src[0]

	        # можно легко спарсить любые другие значения со страницы
	        return ProductsItem(title=title[0], category=category[0], image=image)