from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer,AllProductSerializer,ProfileSerializer
from .serializers import AddressSerializer,OrderSerializer,AdminOrderSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from Product.models import Product,Category
from Profile.models import Visited,Profile,Address,Review,Orders
from django.db import transaction
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt

#Visited page count by date (For each product als0)
#ORders count by date (For each product als0)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def visited_count(request,username):
  user = User.objects.get(username = username)
  products = Product.objects.filter(postedby = user)


  visited_by_date = []
  vis = {}
  for items in products:
    vi = Visited.objects.filter(product = items).values("datetime__date","product").annotate(Count("datetime__date"))
    for j in vi:
      j["Product-name"] = items.name
      if str(j["datetime__date"]) in vis:
        vis[str(j["datetime__date"])] += j['datetime__date__count']
      else:
        vis[str(j["datetime__date"])] = j['datetime__date__count']
    visited_by_date.append(vi)
  visited_by_date.append(vis)

  return Response(visited_by_date)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def orders_count(request,username):

  user = User.objects.get(username = username)
  products = Product.objects.filter(postedby = user)

  orders_by_date = []
  orde = {}
  for items in products:
    ordd = Orders.objects.filter(product = items).values("datetime__date","product").annotate(Count("datetime__date"))
    for j in ordd:
      j["Product-name"] = items.name
      if str(j["datetime__date"]) in orde:
        orde[str(j["datetime__date"])] += j['datetime__date__count']
      else:
        orde[str(j["datetime__date"])] = j['datetime__date__count']
    orders_by_date.append(ordd)
  orders_by_date.append(orde)
  return Response(orders_by_date)
  