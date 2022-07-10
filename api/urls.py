from django.urls import path
from . import views
from . import profileviews
from . import productviews
from . import orderviews
from . import analytics
from . import scraper
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  #pk - page number
  path("allproducts/<str:pk>/",views.get_all_products,name = "all products"),
  #pk - product id
  path("product/<str:pk>/",views.get_product,name  = "product"),
  path("topfive/",views.top_five,name = "Top five"),
  #pk1 - search text
  #pk2 - page number
  path("search/",views.search,name = "Search"),
  #pk1 - Ascending or Descending
  #pk2 - page number
  #pk3 - Search varaible
  path("pricesort/<str:pk1>/<str:pk2>/",views.sort_by_price,name = "Price Sort"),
  path("datetimesort/<str:pk1>/<str:pk2>/",views.sort_by_datetime,name = "Time Sort"),
  path("spricesort/<str:pk1>/<str:pk2>/<str:pk3>/",views.ssort_by_price,name = "Search Price Sort"),
  path("sdatetimesort/<str:pk1>/<str:pk2>/<str:pk3>/",views.ssort_by_datetime,name = "Search Time Sort"),

  #pk- page number
  path("recommended/<str:username>/<str:pk>/",views.recommended_products,name = "Recommended products"),
  
  path("createprofile/",profileviews.create_profile,name = "Create Profile"),
  path("updateprofile/",profileviews.update_profile,name = "Update Profile"),
  path("getprofile/<str:username>/",profileviews.get_profile,name = "Get Profile"),
  path("addaddress/<str:username>/",profileviews.add_address,name = "Add Address"),
  path("getaddress/<str:username>/",profileviews.get_addresses,name = "Get Address"),
  #pk - Address id
  path("deleteaddress/<str:pk>/",profileviews.delete_address,name = "Delete Address"),

  path("addproduct/",productviews.add_product,name = "Add Product"),
  path("updateproduct/",productviews.update_product,name = "Update Product"),
  #pk - Product ID
  path("deleteproduct/<str:pk>/",productviews.delete_product,name = "Delete product"),

  path("addreview/",productviews.add_review,name = "Add Review"),
  path("deletereview/",productviews.delete_review,name = "Delete Review"),

  path("createorder/",orderviews.create_order,name = "Create Order"),
  #pk - username
  path("userorders/<str:pk>/",orderviews.user_orders,name = "User Orders"),
  #pk - username
  path("adminorders/<str:pk>/",orderviews.admin_orders,name = "Admin Orders"),

  path("visitedanalytics/<str:username>/",analytics.visited_count,name = "Visited Analytics"),
  path("ordersanalytics/<str:username>/",analytics.orders_count,name = "Orders Analytics"),

  path("scraper/",scraper.a,name = "a"),

  path("addcart/",orderviews.add_cart,name = "Add to Cart"),
  path("deletecart/",orderviews.delete_cart,name = "Delete frome Cart"),
  path("getcart/<str:pk>",orderviews.get_cart,name = "get cart"),
]