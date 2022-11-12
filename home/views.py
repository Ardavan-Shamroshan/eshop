from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# home page
def index(request):
    return render(request, 'home/index.html')


# contact us page
def contactUs(request):
    return render(request, 'home/contact-us.html')


"""render components, using django-render-partial package
see https://pypi.org/project/django-render-partial/
"""


# header component
def header_component(request):
    context = {}
    return render(request, 'app/partials/header.html', context)


# footer component
def footer_component(request):
    context = {}
    return render(request, 'app/partials/footer.html', context)
