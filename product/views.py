from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import Http404
from django.db.models import Q


# Create your views here.

# Products list
def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product/index.html', context)


# Product detail
def show(request, product_id):
    # try:
    #     product = Product.objects.get(pk=product_id)
    #     context = {
    #         'product': product
    #     }
    # except Exception:
    #     raise Http404()
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'product/show.html', context)
