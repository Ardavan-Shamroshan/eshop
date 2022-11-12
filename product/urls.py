"""product module URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="product"),
    path('<slug:slug>', views.show, name="product.show"),
]
