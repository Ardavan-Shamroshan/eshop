"""product module URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('contact-us/', views.contactUs, name="home.contact-us"),
]
