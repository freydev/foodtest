# -*- coding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField


class Product(models.Model):
	category = models.ForeignKey('Category', verbose_name=u'Категория', null=True, blank=True)

	title = models.CharField(u'Название', max_length=255)
	image = models.SlugField(u'Ссылка на изображение')

	class Meta:
		ordering = ['title']
		verbose_name=u'Продукт с findfood'
		verbose_name_plural=u'Продукты с findfood'

	def __unicode__(self):
		return self.title


class Category(models.Model):
	title = models.CharField(u'Название', max_length=255)

	class Meta:
		ordering = ['title']
		verbose_name=u'Категорию с findfood'
		verbose_name_plural = u'Категории с findfood'

	def __unicode__(self):
		return self.title


class Recipe(models.Model):
	name = models.CharField(u'Название', max_length=255)
	servings = models.CharField(u'Порций', max_length=50)
	directions = HTMLField(u'Направления')
	difficulty = models.CharField(u'Сложность', max_length=50)
	preptime = models.CharField(u'Приготовление', max_length=50)

	class Meta:
		ordering = ['name']
		verbose_name = u'Рецепт с foodrepublic'
		verbose_name_plural = u'Рецепты с foodrepublic'

	def __unicode__(self):
		return self.name


class Ingridient(models.Model):
	SUBCATEGORY = (
		(u'1', u'Beverages/Bar'),
		(u'2', u'Dairy'),
		(u'3', u'Meat/Poultry/Seafood'),
		(u'4', u'Pantry'),
		(u'5', u'Produce'),
	)

	category = models.CharField(u'Категория', choices=SUBCATEGORY, max_length=1, blank=True)
	name = models.CharField(u'Название', max_length=255)

	class Meta:
		ordering = ['name']
		verbose_name=u'Ингридиент'
		verbose_name_plural=u'Ингридиенты'

	def __unicode__(self):
		return self.name