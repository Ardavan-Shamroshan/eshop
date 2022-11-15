from django.contrib import admin
from . import models


# Register your models here.

# The ModelAdmin class is the representation of a model in the admin interface.
# Usually, these are stored in a file named admin.py in your application.
class ContactAdmin(admin.ModelAdmin):
    pass


# contact admin
admin.site.register(models.ContactUs, ContactAdmin)
