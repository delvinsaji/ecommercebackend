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
def get_all_products(request,pk):
  product = Product.objects.all()[((int(pk) - 1)* 8):(int(pk)*8)]
  serializer = AllProductSerializer(product,many = True)
  return Response(serializer.data)


@api_view(['POST'])
def get_product(request,pk):
  req = request.data
  with transaction.atomic():
    try:
      product = Product.objects.get(id = pk)
    except:
      return Response("The product does not exist")
    if req["user"] == "null":
      visited = Visited.objects.create(product= product,category=product.category)
    else:
      visited = Visited.objects.create(user = User.objects.get(username = request.user),product= product,category=product.category)
    visited.save()
  serializer = ProductSerializer(product,many = False)
  return Response(serializer.data)


@api_view(['GET'])
def top_five(request):
  sorted_product = Product.objects.order_by("datetime")[:5]
  serializer = AllProductSerializer(sorted_product,many = True)
  return Response(serializer.data)


@api_view(['GET'])
def search(request):
  data = request.query_params
  s = data['search_value']
  p = data['page']
  try:
    product = Product.objects.filter(Q(name__icontains = s) | Q(category = Category.objects.get(category = pk1.capitalize())))[(((int(p)) - 1)* 8):(int(p)*8)]
  except:
    product = Product.objects.filter(name__icontains = s)[(((int(p)) - 1)* 20):(int(p)*20)]
  serializer = AllProductSerializer(product,many  = True)
  return Response(serializer.data)



@api_view(['GET'])
def sort_by_price(request,pk1,pk2):
  if pk1 == '0':
    product = Product.objects.order_by('price')[((int(pk2) - 1)* 8):(int(pk2)*8)]
  else:
    product = Product.objects.order_by('-price')[((int(pk2) - 1)* 8):(int(pk2)*8)]
  serializer = AllProductSerializer(product,many = True)
  return Response(serializer.data)

@api_view(['GET'])
def sort_by_datetime(request,pk1,pk2):
  if pk1 == '0':
    product = Product.objects.order_by('datetime')[((int(pk2) - 1)* 8):(int(pk2)*8)]
  else:
    product = Product.objects.order_by('-datetime')[((int(pk2) - 1)* 8):(int(pk2)*8)]
  serializer = AllProductSerializer(product,many = True)
  return Response(serializer.data)



@api_view(['GET'])
def ssort_by_price(request,pk1,pk2,pk3):
  if pk1 == '0':
    try:
      product = Product.objects.filter(Q(name__icontains = pk3) | Q(category = Category.objects.get(category = pk3.capitalize()))).order_by('price')[((int(pk2) - 1)* 8):(int(pk2)*8)]
    except:
      product = Product.objects.filter(name__icontains = pk3)
  else:
    try:
      product = Product.objects.filter(Q(name__icontains = pk3) | Q(category = Category.objects.get(category = pk3.capitalize()))).order_by('-price')[((int(pk2) - 1)* 8):(int(pk2)*8)]
    except:
      product = Product.objects.filter(name__icontains = pk3)
  serializer = AllProductSerializer(product,many = True)
  return Response(serializer.data)


@api_view(['GET'])
def ssort_by_datetime(request,pk1,pk2,pk3):
  if pk1 == '0':
    try:
      product = Product.objects.filter(Q(name__icontains = pk3) | Q(category = Category.objects.get(category = pk3.capitalize()))).order_by('datetime')[((int(pk2) - 1)* 8):(int(pk2)*8)]
    except:
      product = Product.objects.filter(name__icontains = pk3)
  else:
    try:
      product = Product.objects.filter(Q(name__icontains = pk3) | Q(category = Category.objects.get(category = pk3.capitalize()))).order_by('-datetime')[((int(pk2) - 1)* 8):(int(pk2)*8)]
    except:
      product = Product.objects.filter(name__icontains = pk3)
  serializer = AllProductSerializer(product,many = True)
  return Response(serializer.data)


@api_view(['GET'])
def recommended_products(request,username,pk):
  if username == " ":
    return Response(False)

  visited = Visited.objects.filter(user = User.objects.get(username = username))
  visited_count = visited.values('category').annotate(Count('category')).order_by('-category__count')

  try:
    most_visited = visited_count[0]
    category = most_visited['category']
    product = Product.objects.filter(category = category)[((int(pk2) - 1)* 8):(int(pk2)*8)]
    serializer = AllProductSerializer(product,many = True)
  except:
    return Response(False)
  return Response(serializer.data)