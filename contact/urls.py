"""contact module URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    # function base view url
    # path('', views.contact_us, name='contact'),

    # class base view url
    path('', views.ContactUsView.as_view(), name='contact'),
    path('profile', views.CreateProfileView.as_view(), name='contact.profile'),
    path('profile-list', views.ProductListView.as_view(), name='contact.profile-list'),
]
