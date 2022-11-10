from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'home/index.html')


def contactUs(request):
    return render(request, 'home/contact-us.html')
