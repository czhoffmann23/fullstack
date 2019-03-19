# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .scraperroutine import *
from .services import *
import json


def index(request):
    return render(request, 'scraper/index.html')
    
def category(request):
    all_category = GetCategorys()
    context={
       'all_category':all_category,
    }
    
    return render(request,'scraper/category.html',context)



def tablecontent(request,categoryname):
    all_category          = GetCategorys()
    category,url_category = GetCategoryNameUrlObject(categoryname)
    all_books             = GetUrlBooksData(url_category,category)
    text                  = categoryname
    context               = {

       'all_books':all_books,
       'all_category':all_category,
       'text': text

    }

    if(all_books==None):
        url='/category/'+str(categoryname)
        return redirect(url)
    else:
        return render(request,'scraper/tableContent.html',context)

def detailproduct(request,categoryname,id):
    all_category = GetCategorys()
    one_book=GetBookObject(id)
    text = categoryname
    id_book = one_book[0]['id']
    context={
       'one_book':one_book,
       'text': text,
       'id_book': id_book,
       'all_category':all_category
    }
   
    return render(request,'scraper/detailProduct.html',context)
    
def delete(request,categoryname,id):
    try:
        one_book = DeleteBookObject(id,categoryname)
        messages.success(request,'Succesfull Delete.')
        url='/category/'+str(categoryname)
        return redirect(url)
    except (keyError):
        return redirect(request, 'scraper/detailProduct.html',{'error_message': "I can't delete the product"})
