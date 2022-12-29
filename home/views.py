from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView


# Create your views here.


# class based view
# class HomeView(View):
#     def get(self, request):
#         context = {
#             'data': 'This is Data'
#         }
#         return render(request, 'home/index.html', context)


class HomeView(TemplateView):
    template_name = 'home/index.html'

    # context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = 'This is Data in template view'
        return context


# function based view
# home page
# def index(request):
#     return render(request, 'home/index.html')


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
