from django.contrib import admin


# Register your models here.

from .models import Profile,Address,Cart,Review,Visited,Orders

admin.site.register([Profile,Address,Cart,Review,Visited,Orders])