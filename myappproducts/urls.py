from django.contrib import admin
from django.urls import path, include
from myappproducts import views


urlpatterns = [
    path('product/(?P<product_id>\w+)/$', views.product, name='product'),
]