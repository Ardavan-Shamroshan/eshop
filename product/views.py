from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import Http404
from django.db.models import Q, Avg


# Create your views here.

# Products list
def index(request):
    products = Product.objects.all().order_by('title')
    total_products_count = products.count()
    rating_average = products.aggregate(Avg("rating"))
    context = {
        'products': products,
        'total_products_count': total_products_count,
        'rating_average': rating_average
    }
    return render(request, 'product/index.html', context)


# Product detail
def show(request, product_slug):
    # try:
    #     product = Product.objects.get(pk=product_id)
    #     context = {
    #         'product': product
    #     }
    # except Exception:
    #     raise Http404()
    product = get_object_or_404(Product, slug=product_slug)
    context = {
        'product': product
    }
    return render(request, 'product/show.html', context)
