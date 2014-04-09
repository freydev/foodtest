# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ProductsItem(Item):
	title = Field()
	category = Field()
	image = Field()


class RecipesItem(Item):
	name = Field()
	servings = Field()
	directions = Field()
	difficulty = Field()
	preptime = Field()
