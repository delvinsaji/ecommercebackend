from rest_framework import serializers
from Profile.models import Profile,Address,Cart,Review,Visited,Orders
from Product.models import Category,Product
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["username"]

class ReviewSerializer(serializers.ModelSerializer):
  username = serializers.SerializerMethodField("get_user")

  class Meta:
    model = Review
    fields = "__all__"

  def get_user(self,review):
    user = review.user
    serilaizer = UserSerializer(user,many = False)
    return serilaizer.data


class ProductSerializer(serializers.ModelSerializer):
  product_reviews = serializers.SerializerMethodField("get_reviews")

  class Meta:
    model = Product
    fields = "__all__"

  def get_reviews(self,product):
    reviews = Review.objects.filter(product=product)
    serializer = ReviewSerializer(reviews,many = True)
    return serializer.data

class AllProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):
  class Meta:
    model = Address
    fields = "__all__"

class Product1Serializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
  products = serializers.SerializerMethodField("get_products")

  class Meta:
    model = Orders
    fields = "__all__"

  def get_products(self,orders):
    product = Product.objects.get(id = orders.product.id)
    serializer = Product1Serializer(product,many = False)
    return serializer.data

class ProfileSerializer(serializers.ModelSerializer):
  products = serializers.SerializerMethodField('get_products')
  addresses = serializers.SerializerMethodField("get_addresses")
  user = serializers.SerializerMethodField("get_username")
  orders = serializers.SerializerMethodField("get_orders")

  class Meta:
    model = Profile
    fields = "__all__"

  def get_products(self,profile):
    products = Product.objects.filter(postedby = profile.user)
    serializer = AllProductSerializer(products,many = True)
    return serializer.data

  def get_addresses(self,profile):
    address = Address.objects.filter(user = profile.user)
    serializer = AddressSerializer(address,many = True)
    return serializer.data

  def get_username(self,profile):
    user = profile.user
    serializer = UserSerializer(user,many = False)
    return serializer.data

  def get_orders(self,profile):
    orders = Orders.objects.filter(user = profile.user).order_by('datetime')
    serializer = OrderSerializer(orders,many = True)
    return serializer.data

class AdminOrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Orders
    fields = ["datetime","quantity","product"]

class CartSerializer(serializers.ModelSerializer):
  product = serializers.SerializerMethodField('get_product')

  class Meta:
    model = Cart
    fields = "__all__"

  def get_product(self,cart):
    product = Product.objects.get(id = cart.product.id)
    serializer = ProductSerializer(product,many = False)
    return serializer.data
