from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory


# Create your views here.

# Products list
def index(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all().order_by('title')
    total_products_count = products.count()
    context = {
        'products': products,
        'categories': categories,
        'total_products_count': total_products_count,
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
