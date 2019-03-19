from .models import Category,Books
import json

def GetCategoryNameUrlObject(name):
    CategoryObject = Category.objects.filter(name=name).values('name','url_name')
    return CategoryObject[0]['name'],CategoryObject[0]['url_name']

def GetBookObject(id):
    BookObject = Books.objects.filter(id=id).values('category','tittle','thumbnail','price','stock','product_description','upc', 'id')
    return BookObject

def DeleteBookObject(id,categoryname):
    BookObject =  Books.objects.get(pk=id).delete()
    return BookObject