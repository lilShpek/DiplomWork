from django.contrib import admin
from django.urls import path, include
from myapporders import views

urlpatterns = [
    path('basket_adding/', views.basket_adding, name='basket_adding'),
    path('checkout/', views.checkout, name='checkout'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
]