from django.contrib import admin
from django.urls import path,include
from Home import views

admin.site.site_header = "Unish Resturants Admin"
admin.site.site_title = "Unish Resturants Portal"
admin.site.index_title = "Welcome to Unish Resturants Portal"

urlpatterns = [
    path('', views.index, name='Home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('food', views.food, name='food'),
    path('drinks', views.drinks, name='drinks')
    ]
