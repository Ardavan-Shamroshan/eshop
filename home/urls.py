"""product module URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    # function based url
    # path('', views.index, name="home"),

    # class based url
    path('', views.HomeView.as_view(), name="home"),
]
