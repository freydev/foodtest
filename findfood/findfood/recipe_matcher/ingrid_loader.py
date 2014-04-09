# -*- coding: utf-8 -*-
# выполняется непосредственно из директории со скриптом
# PYTHONPATH=../.. DJANGO_SETTINGS_MODULE=findfood.settings python ingrid_loader.py

from findfood.models import Ingridient
import re

bev__bar = open('beverages_bar.html').read()
dairy = open('dairy.html').read()
meat = open('meat.html').read()
pantry = open('pantry.html').read()
produce = open('produce.html').read()

data_files = [bev__bar, dairy, meat, pantry, produce]
pattern = 'ingredient">([^&]*)</span>'

for dataset in list(enumerate(data_files, start=1)):
	category = dataset[0]
	for ingr in re.findall(pattern, dataset[1]):
		obj, _ = Ingridient.objects.get_or_create(name=ingr)
		obj.category = category
		obj.save()