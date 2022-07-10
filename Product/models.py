from django.db import models

# Create your models here.
from django.db import models
import uuid
from django.contrib.auth.models import User

class Category(models.Model):
  id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key = True)
  category = models.CharField(max_length = 300,null = True,blank = True)

  def __str__(self):
    return self.category

class Product(models.Model):
  status = (
    ("In Stock","Available"),
    ("Out of Stock","Out of Stock")
  )
  id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key = True)
  name = models.CharField(max_length = 500,null = True,blank=True)
  price = models.IntegerField(null = True,blank = True)
  desciption = models.TextField(null = True,blank = True)
  status = models.CharField(max_length = 200, choices=status,null = True,blank=True)
  category = models.ForeignKey(Category, on_delete = models.CASCADE,null = True,blank = True)
  postedby = models.ForeignKey(User, on_delete = models.CASCADE,null = True,blank = True)
  image = models.TextField(default = "https://images.freeimages.com/images/small-previews/a4f/empty-box-1160649.jpg")
  rating = models.FloatField(null = True,blank = True)
  datetime = models.DateTimeField(auto_now_add=True)
#image left


  def __str__(self):
    return self.name