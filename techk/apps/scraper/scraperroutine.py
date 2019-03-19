# -*- coding: utf-8 -*-
#!/usr/bin/python
from bs4 import BeautifulSoup
from .models import Category,Books
from django.shortcuts import redirect
import requests
import json

#Make BeautifulSoup
def CallBeautifulSoup(website_url):
    get_website    = requests.get(website_url)
    data_website   = get_website.text
    return  BeautifulSoup(data_website,"html.parser")


#Get categorys by website
def GetCategorys():
    all_category = Category.objects.all()
    if(all_category):
        #all_category= Category.objects.all().delete()
        #Books.objects.all().delete()
        return all_category
    else:
        website        = "http://books.toscrape.com/index.html"
        url_category   = "http://books.toscrape.com/"
        soup    = CallBeautifulSoup(website)
        for item in soup.select("ul.nav-list li ul li a"):
            new_category = Category(name=(item.text).strip(),url_name=url_category + item['href'])
            new_category.save()
                
        all_category = Category.objects.all()
        return all_category


def GetBookData(url_product,category):
    soup          = CallBeautifulSoup(url_product)
    url_thumbnail ="http://books.toscrape.com"
    thumbnail     = soup.select_one("div.active img")
    price         = soup.select_one("p.price_color")
    stock         = soup.select_one("p.availability")
    description   = soup.find('p', class_=False)
    upc           = soup.find_all('td')
    tittle        = thumbnail['alt']
    thumbnail     = url_thumbnail + (thumbnail['src'])[5:len(thumbnail['src'])]
    price         = price.text
    stock         = (stock.text).strip()
    upc           = upc[0].get_text()
    try: #manage exception for time of process
        description = description.text 
        new_book    = Books(category=category,tittle=tittle,thumbnail=thumbnail,price=price,stock=stock,product_description=description,upc=upc)
        new_book.save()
    except:
        pass
   

cont_flag=0

#Get Books Data by url of category
def GetUrlBooksData(url_cat,categoryChoose):
    all_books = Books.objects.all().filter(category=categoryChoose)
    if(all_books):
        return all_books
    else:
        global cont_flag
        cont_flag = cont_flag + 1
        soup      = CallBeautifulSoup(url_cat)
        url_category   = "http://books.toscrape.com/catalogue/"
        for item in soup.select("section div ol.row li article.product_pod div.image_container a"):
            item_url = url_category + (item['href'])[9:len(item['href'])]
            GetBookData(item_url,categoryChoose)

        button_next = soup.select_one("li.next a") 
        if(button_next != None):
            if(cont_flag == 1):
                url_nextpage = url_cat[:-10] + button_next['href']
            if(cont_flag>1):
                url_nextpage = url_cat[:-11] + button_next['href']
            GetUrlBooksData(url_nextpage,categoryChoose)
        else:
            cont_flag = 0
            all_books = Books.objects.all().filter(category=categoryChoose)
            return all_books
   




