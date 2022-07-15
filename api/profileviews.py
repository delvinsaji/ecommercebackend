from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer,AllProductSerializer,ProfileSerializer
from .serializers import AddressSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from Product.models import Product,Category
from Profile.models import Visited,Profile,Address


@api_view(['POST'])
def create_profile(request):
  request = request.data
  try:
    user = User.objects.get(username = username)
    return Response("The username already exists")
  except:
    pass

  user = User.objects.create_user(username = request['username'])
  user.set_password(request['password'])
  user.save()

  profile = Profile.objects.create(name = request['name'],user = user,
                          email = request['email'],
                          age = request['age'])
  profile.save()

  return Response("Successfully Created")



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_profile(request,username):
  request = request.data


  user = User.objects.get(username = username)
  profile = Profile.objects.get(user = user)

  profile.name = request['name']
  profile.email = request['email']
  profile.age = request['age']
  profile.save()

  if request['username'] != username:
    try:
      exist = User.objects.get(username = request['username'])
      return Response("username already exists")
    except:
      user.username = request['username']
      user.save()

  return Response("Successfully updated")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_password(request,username):
  r = request.data

  user = User.objects.get(username = username)

  if user.check_password(r['old_password']):
    user.set_password(r['new_password'])
    user.save()
  else:
    return Response("The password entered is incorrect")
  return Response("Password changed")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request,username):
  profile = Profile.objects.get(user = User.objects.get(username = username))
  serializer = ProfileSerializer(profile,many = False)
  return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_address(request,username):
  req = request.data
  user = User.objects.get(username = username)
  address = Address.objects.create(user = user,houseName = req['houseName'],
                                  cityName = req['cityName'],stateName = req['stateName'],
                                  pin = req['pin'])
  address.save()
  return Response("Address Added")



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_addresses(request,username):
  address = Address.objects.filter(user = User.objects.get(username = username))
  serializer = AddressSerializer(address,many = True)
  return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_address(request,pk):
  address = Address.objects.get(id = pk)
  address.delete()
  return Response("Successfully deleted")