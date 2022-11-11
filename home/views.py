from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# home page
def index(request):
    return render(request, 'home/index.html')


# contact us page
def contactUs(request):
    return render(request, 'home/contact-us.html')


# header partial
def header_partial(request):
    context = {}
    return render(request, 'app/partials/header.html', context)
