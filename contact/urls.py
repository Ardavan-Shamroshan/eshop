"""contact module URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    # function base view url
    # path('', views.contact_us, name='contact'),

    # class base view url
    path('', views.ContactUsView.as_view(), name='contact'),
]
