from django.contrib import admin
from . import models


# Register your models here.

# The ModelAdmin class is the representation of a model in the admin interface.
# Usually, these are stored in a file named admin.py in your application.
class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = [
        'title',
        'price',
        'summary',
        'rating',
        'is_active',
    ]
    list_filter = [
        'rating',
        'is_active'
    ]
    list_editable = [
        'is_active'
    ]


admin.site.register(models.Product, ProductAdmin)
