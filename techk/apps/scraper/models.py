# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name         = models.CharField(max_length=100, default= '')
    url_name     = models.URLField(default='')

    def __str__(self):
        return self.name

class Books(models.Model):
    category            =  models.CharField(max_length=100, default= '')
    tittle              =  models.CharField(max_length=60, default= '')
    thumbnail           =  models.CharField(max_length=150, default= '')
    price               =  models.CharField(max_length=150,default='')
    stock               =  models.CharField(max_length=150,default='')
    product_description =  models.CharField(max_length=300, default= '')
    upc                 =  models.CharField(max_length=150, default= '') 