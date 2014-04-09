# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from findfood.models import Category, Product, Recipe

class ProductsPipeline(object):
    def process_item(self, item, spider):

        if spider.name not in 'products':
            # не наша линия, идем дальше
            return item

        if item['category']:
            category, _ = Category.objects.get_or_create(title=item['category'])
            product, _ = Product.objects.get_or_create(title=item['title'])

            product.category=category 
            product.image=item['image']
            product.save()

        return item


class RecipesPipeline(object):
    def process_item(self, item, spider):

        if spider.name not in 'recipes':
            # не наша линия, идем дальше
            return item

        recipe, _ = Recipe.objects.get_or_create(name=item['name'].strip())
        recipe.servings = item['servings'].strip()
        recipe.difficulty = item['difficulty'].strip()
        recipe.directions = item['directions'].strip()
        recipe.preptime = item['preptime'].strip()
        recipe.save()

        return item