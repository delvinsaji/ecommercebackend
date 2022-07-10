from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer,AllProductSerializer,ProfileSerializer
from .serializers import AddressSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from Product.models import Product,Category
from Profile.models import Visited,Profile,Address,Review
from django.db import transaction


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product(request):
  r = request.data
  user = User.objects.get(username = r['username'])
  category = Category.objects.get(category = r['category'])

  product = Product.objects.create(name = r['name'],price = r['price'],desciption = r['description'],
                                  postedby = user,image = r['image'],status = r['status'],
                                  category=category)
  product.save()
  return Response("Product Added")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_product(request,pk):
  r = request.data

  category = Category.objects.get(category = r['category'])

  product = Product.objects.get(id = pk)
  product.name = r['name']
  product.price = r['price']
  product.desciption = r['description']
  product.image = r['image']
  product.status = r['status']
  product.category = category
  product.save()

  return Response("Product updated")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def delete_product(request,pk):
  product = Product.objects.get(id = pk)
  product.delete()
  return Response("Successfully deleted")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_review(request):
  r = request.data

  with transaction.atomic():
    product = Product.objects.get(id = r['id'])
    user = User.objects.select_for_update().get(username = r['username'])
    try:
      review = Review.objects.get(user = user)
      return Response("Review already exists")
    except:
      review = Review.objects.create(product=product,rating = r['rating'],user = user,desc = r['description'])
    review.addrating
    review.save()
    return Response("Review added successfully")

  return Response("An error occured")

  
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_review(request):
  r = request.data

  user = User.objects.get(username = r['username'])
  product = Product.objects.get(id = r['id'])

  review = Review.objects.get(user = user,product = product)
  review.deleterating
  review.delete()

  return Response("Review.deleted")