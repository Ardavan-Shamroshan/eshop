from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Product, ProductCategory


# Create your views here.

# Class base view

# ListView
# Product list
class ProductListView(ListView):
    template_name = 'product/index.html'
    model = Product
    # changes the name of context object from object_list
    context_object_name = 'products'

    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        data = base_query.filter(is_active=True)
        return data


# Product detail
class ProductDetailView(DetailView):
    template_name = 'product/show.html'
    model = Product


# TemplateView
# Product list
# class ProductListView(TemplateView):
#     template_name = 'product/index.html'
#     # get context data
#
#     def get_context_data(self, **kwargs):
#         products = Product.objects.all().order_by('-price')[:5]
#         context = super(ProductListView, self).get_context_data()
#         context['products'] = products
#         return context


# Product detail
# class ProductDetailView(TemplateView):
#     template_name = 'product/show.html'
#
#     # get context data
#     def get_context_data(self, **kwargs):
#         # get slug from key-word-arguments
#         slug = kwargs['slug']
#         product = get_object_or_404(Product, slug=slug)
#         context = super(ProductDetailView, self).get_context_data()
#         context['product'] = product
#         return context


# Function base view
# Products list
# def index(request):
#     products = Product.objects.all().order_by('-price')[:5]
#     total_products_count = products.count()
#     context = {
#         'products': products,
#         'total_products_count': total_products_count,
#     }
#     return render(request, 'product/index.html', context)
#
#
# # Product detail
# def show(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     context = {
#         'product': product
#     }
#     return render(request, 'product/show.html', context)


"""render components, using django-render-partial package
see https://pypi.org/project/django-render-partial/
"""


# sidebar component
def sidebar_component(request):
    return render(request, 'components/sidebar.html')


# product item component
def product_item_component(request, *args, **kwargs):
    return render(request, 'components/product-item.html', kwargs)
