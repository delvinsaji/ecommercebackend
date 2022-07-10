import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer,AllProductSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from Product.models import Product,Category
from Profile.models import Visited,Profile
from django.db.models import Q
from django.db.models import Count
from django.db import transaction







@api_view(['GET'])
def a(request):

  r = requests.get("https://www.flipkart.com/search?q=tablets&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
  #Laptops  -  https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_6_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptop%7CLaptops&requestId=c1abc4bb-1291-4845-905d-31709f2a7257&as-backfill=on
  #Smartphones  -https://www.flipkart.com/search?q=smartphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&as-pos=1&as-type=RECENT&suggestionId=smartphone%7CMobiles&requestId=789851fc-5591-4767-ac7c-656ed6311af5&as-searchtext=smartphones


  soup = BeautifulSoup(r.content,'html.parser')
  name = soup.findAll('div',class_ = "_4rR01T")
  names = []
  for items in name:
    names.append(items.text)
  image = soup.findAll('img',class_ = '_396cs4 _3exPp9')
  images = []
  for items in image:
    images.append(items['src'])
  price = soup.findAll('div',class_ = '_30jeq3 _1_WHN1')
  prices = []
  for items in price:
    prices.append(items.text)
  ul = soup.findAll('ul',class_ = '_1xgFaf')
  lis = []
  for items in ul:
    li = items.findAll('li')
    l = []
    for a in li:
      l.append(a.text)
    lis.append(' '.join(l))
  user = User.objects.get(username = 'delvinsaji')
  category = Category.objects.get(category = 'Tablet')
  for i in range(len(names)):
    price = prices[i][1:].replace(',','')
    product = Product.objects.create(name = names[i],price = int(price),desciption = lis[i],image=images[i],postedby = user,
                                    category = category,status = 'In Stock')
    product.save()

  r = requests.get("https://www.flipkart.com/search?q=smartphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&as-pos=1&as-type=RECENT&suggestionId=smartphone%7CMobiles&requestId=789851fc-5591-4767-ac7c-656ed6311af5&as-searchtext=smartphones")
  soup = BeautifulSoup(r.content,'html.parser')
  name = soup.findAll('div',class_ = "_4rR01T")
  names = []
  for items in name:
    names.append(items.text)
  image = soup.findAll('img',class_ = '_396cs4 _3exPp9')
  images = []
  for items in image:
    images.append(items['src'])
  price = soup.findAll('div',class_ = '_30jeq3 _1_WHN1')
  prices = []
  for items in price:
    prices.append(items.text)
  ul = soup.findAll('ul',class_ = '_1xgFaf')
  lis = []
  for items in ul:
    li = items.findAll('li')
    l = []
    for a in li:
      l.append(a.text)
    lis.append(' '.join(l))
  user = User.objects.get(username = 'delvinsaji')
  category = Category.objects.get(category = 'Smartphone')
  for i in range(len(names)):
    price = prices[i][1:].replace(',','')
    product = Product.objects.create(name = names[i],price = int(price),desciption = lis[i],image=images[i],postedby = user,
                                    category = category,status = 'In Stock')
    product.save()

  r = requests.get("https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_6_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptop%7CLaptops&requestId=c1abc4bb-1291-4845-905d-31709f2a7257&as-backfill=on")
  soup = BeautifulSoup(r.content,'html.parser')
  name = soup.findAll('div',class_ = "_4rR01T")
  names = []
  for items in name:
    names.append(items.text)
  image = soup.findAll('img',class_ = '_396cs4 _3exPp9')
  images = []
  for items in image:
    images.append(items['src'])
  price = soup.findAll('div',class_ = '_30jeq3 _1_WHN1')
  prices = []
  for items in price:
    prices.append(items.text)
  ul = soup.findAll('ul',class_ = '_1xgFaf')
  lis = []
  for items in ul:
    li = items.findAll('li')
    l = []
    for a in li:
      l.append(a.text)
    lis.append(' '.join(l))
  user = User.objects.get(username = 'delvinsaji')
  category = Category.objects.get(category = 'Laptop')
  for i in range(len(names)):
    price = prices[i][1:].replace(',','')
    product = Product.objects.create(name = names[i],price = int(price),desciption = lis[i],image=images[i],postedby = user,
                                    category = category,status = 'In Stock')
    product.save()
  return Response("aa")


