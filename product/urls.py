"""product module URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="product"),
    path('<int:product_id>', views.show, name="product.show"),
]
