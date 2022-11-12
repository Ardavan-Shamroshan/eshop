from django.contrib import admin
from . import models


# Register your models here.

# The ModelAdmin class is the representation of a model in the admin interface.
# Usually, these are stored in a file named admin.py in your application.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }

    list_filter = ('category', 'is_active', 'brand', 'created_at', 'updated_at')

    list_display = ('title', 'price', 'is_active', 'is_delete', 'created_at', 'updated_at')

    list_editable = ()


class ProductCategoryAdmin(admin.ModelAdmin):
    pass


class ProductTagAdmin(admin.ModelAdmin):
    pass


class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')


# product admin
admin.site.register(models.Product, ProductAdmin)
# product category admin
admin.site.register(models.ProductCategory, ProductCategoryAdmin)
# product tag admin
admin.site.register(models.ProductTag, ProductTagAdmin)
# product brand admin
admin.site.register(models.ProductBrand, ProductBrandAdmin)
