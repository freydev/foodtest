# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Category, Product, Recipe, Ingridient


class ProductAdmin(admin.ModelAdmin):
	def image_tag(self, item):
	    return u'<img width="64" height="64" src="%s" />' % item.image
	image_tag.short_description = u'Изображение'
	image_tag.allow_tags = True

	list_filter = ('category',)
	list_display = ('title', 'category', 'image_tag')


class RecipesAdmin(admin.ModelAdmin):
	list_display = ('name', 'servings', 'difficulty', 'preptime')


class IngridAdmin(admin.ModelAdmin):
	list_display = ('name', 'category')
	list_filter = ('category',)

# admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Recipe, RecipesAdmin)
admin.site.register(Ingridient, IngridAdmin)