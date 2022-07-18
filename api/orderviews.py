from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer,AllProductSerializer,ProfileSerializer
from .serializers import AddressSerializer,OrderSerializer,AdminOrderSerializer,CartSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from Product.models import Product,Category
from Profile.models import Visited,Profile,Address,Review,Orders,Cart
from django.db import transaction


@api_view(['POST'])
def create_order(request):
  username = request.data['username']
  user = User.objects.get(username = username)

  r = request.data['li']

  for items in r:
    product = Product.objects.get(id = items['id'])
    address = Address.objects.get(id = items['aid'])
    order = Orders.objects.create(user = user,product = product,
                                  address = address,delivered = False,
                                  quantity = items['quantity'])
    order.save()

  return Response("Order generated")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_orders(request,pk):
  user = User.objects.get(username = pk)
  order = Orders.objects.filter(user = user)
  serializer = OrderSerializer(order,many = True)
  return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_orders(request,pk):
  user = User.objects.get(username = pk)
  product = Product.objects.filter(postedby = user)
  li = []
  for items in product:
    order = Orders.objects.filter(product = items)
    for j in order:
      li.append(j)
  serializer = AdminOrderSerializer(li,many = True)
  return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_cart(request):
  r = request.data
  user = User.objects.get(username = r['username'])
  product = Product.objects.get(id = r['product'])
  try:
    cart = Cart.objects.get(product = product)
    return Response("The item is already in cart")
  except:
    pass
  
  cart = Cart.objects.create(user = user,product = product,quantity = r['quantity'])
  cart.save()

  return Response("Added to Cart")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_cart(request):
  r = request.data
  user = User.objects.get(username = r['username'])
  product = Product.objects.get(id = r['product'])

  cart = Cart.objects.get(user = user,product = product)
  cart.delete()

  return Response("Deleted")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cart(request,pk):
  user = User.objects.get(username = pk)
  cart = Cart.objects.filter(user = user)
  serializer = CartSerializer(cart,many = True)
  return Response(serializer.data)
