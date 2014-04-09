from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request

from scrapy.spider import Spider

from food.items import RecipesItem


class RecipesSpider(Spider):
    name = 'recipes'
    allowed_domains = ['foodrepublic.com']
    start_urls = ['http://www.foodrepublic.com/recipes']


    def parse(self, response):
        sel = Selector(response)
        links = sel.xpath('//div[contains(@class, "recipe-link")]/a/@href')
        next_link = sel.xpath('//*[@id="content-area"]/div/div/div/div/div/div/div[2]/ul/li/a/@href').extract() or ['None']
        if next_link:
            request = Request('http://%s%s' %(self.allowed_domains[0], next_link.pop()), callback=self.parse)
            yield request

        for link in links.extract():
            request = Request('http://%s%s' %(self.allowed_domains[0], link), callback=self.parse_recipe)
            yield request


    def parse_recipe(self, response):
        sel = Selector(response)
        title = sel.xpath('//*[@id="content-area"]/div/span/h1/text()').extract() or ['None']
        servings = sel.xpath('//*[@id="content-area"]/div/div[6]/div[3]/div/span/text()').extract() or ['None']
        directions = sel.xpath('//*[@id="content-area"]/div/div[6]/div[5]/div[2]/div').extract() or ['None']
        difficulty = sel.xpath('//*[@id="content-area"]/div/div[6]/div[6]/div[2]/div/text()').extract() or ['None']
        preptime = sel.xpath('//*[@id="content-area"]/div/div[6]/div[7]/div[2]/div/span/text()').extract() or ['None']

        return RecipesItem(
            name=title.pop().replace('Recipe', ''), 
            servings=servings.pop(), 
            directions=directions.pop(), 
            difficulty=difficulty.pop(),
            preptime=preptime.pop(),
        )