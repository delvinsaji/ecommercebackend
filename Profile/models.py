from django.db import models

# Create your models here.
from Product.models import Product,Category
from django.db import models
import uuid
from django.contrib.auth.models import User

class Profile(models.Model):
  name = models.CharField(max_length = 200,null = True,blank = True)
  user = models.OneToOneField(User,on_delete=models.CASCADE,null = True,blank = True)
  id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key = True)
  email = models.EmailField(null = True,blank = True)
  age = models.IntegerField(null = True,blank= True)

  def __str__(self):
    return self.name

class Address(models.Model):
  id = models.UUIDField(default=uuid.uuid4,primary_key=True)
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  houseName = models.CharField(max_length = 1000,null = True,blank=True)
  cityName = models.CharField(max_length = 1000,null = True,blank=True)
  stateName = models.CharField(max_length = 1000,null = True,blank=True)
  pin = models.IntegerField(null = True,blank = True)

  def __str__(self):
    return self.user.username

class Cart(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  product = models.ForeignKey(Product, on_delete = models.CASCADE)
  quantity = models.IntegerField(null = True,blank = True)

  def __str__(self):
    return self.user.username

class Review(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  product = models.ForeignKey(Product, on_delete = models.CASCADE)
  rating = models.IntegerField(null = True,blank=True)
  date = models.DateTimeField(auto_now_add=True)
  desc = models.TextField(null = True,blank = True)


  def __str__(self):
    return self.user.username

  @property
  def addrating(self):
    rat = self.product.rating
    product = Product.objects.get(name = self.product.name)
    if rat is None:
      product.rating = self.rating
      product.save()
    else:
      count = Review.objects.filter(product = self.product).count()
      final = ((rat * (count - 1)) + self.rating)/count
      product.rating = final
      product.save()

  @property
  def deleterating(self):
    rat = self.product.rating
    product = Product.objects.get(name = self.product.name)
    count = Review.objects.filter(product = self.product).count()
    final_rat = (rat * count) -  self.rating
    product.rating = final_rat/(count-1)
    product.save()


class Visited(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE,null = True,blank = True)
  product = models.ForeignKey(Product, on_delete = models.CASCADE)
  category = models.ForeignKey(Category, on_delete = models.CASCADE,null = True,blank = True)
  datetime = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.product.name


class Orders(models.Model):
  id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key = True)
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  product = models.ForeignKey(Product, on_delete = models.CASCADE)
  datetime = models.DateTimeField(auto_now_add=True)
  delivered = models.BooleanField(null = True,blank = True,default = False)
  address = models.ForeignKey(Address, on_delete = models.CASCADE)
  quantity = models.IntegerField(null = True, blank = True)

