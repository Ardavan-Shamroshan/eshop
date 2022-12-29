"""product module URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    # function base urls
    # path('', views.index, name="product"),
    # path('<slug:slug>', views.show, name="product.show"),

    # class base urls
    path('', views.ProductListView.as_view(), name='product'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product.show'),
    # path('<int:pk>', views.ProductDetailView.as_view(), name='product.show'),

]
