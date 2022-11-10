from django.contrib import admin
from . import models


# Register your models here.

# The ModelAdmin class is the representation of a model in the admin interface.
# Usually, these are stored in a file named admin.py in your application.
class ProductAdmin(admin.ModelAdmin):
    pass


class ProductCategoryAdmin(admin.ModelAdmin):
    pass


class ProductTagAdmin(admin.ModelAdmin):
    pass


# product admin
admin.site.register(models.Product, ProductAdmin)
# product category admin
admin.site.register(models.ProductCategory, ProductCategoryAdmin)
# product tag admin
admin.site.register(models.ProductTag, ProductTagAdmin)
