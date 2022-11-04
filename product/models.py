from django.core.validators import *
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

# product categories (one to many)
class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url')

    # to display an object in the Django admin site and as the value inserted into a template
    def __str__(self):
        return f"{self.title}"


# product information (one to one)
class ProductInformation(models.Model):
    color = models.CharField(max_length=200, verbose_name='رنگ')
    size = models.CharField(max_length=200, verbose_name='اندازه')

    def __str__(self):
        return f'{self.color} {self.size}'


# products
class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory, null=True, blank=True, on_delete=models.CASCADE, related_name='products')
    information = models.OneToOneField(ProductInformation, verbose_name='اطلاعات تکمیلی', null=True, blank=True, on_delete=models.CASCADE, related_name='information')
    price = models.IntegerField()
    rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ], default=0)
    summary = models.CharField(max_length=350, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(default='', null=False, db_index=True)

    # to display an object in the Django admin site and as the value inserted into a template
    # when it displays an object.
    # Thus, you should always return a nice, human-readable representation of the model
    # from the __str__() method.
    def __str__(self):
        return f"{self.title} ({self.price})"

    # define a get_absolute_url() method to tell Django how to calculate the canonical URL for an object.
    # To callers, this method should appear to return a string that can be used to refer to the object over HTTP.
    def get_absolute_url(self):
        # While this code is correct and simple, it may not be the most portable way to write this kind of method.
        # The reverse() function is usually the best approach.
        return reverse('product.show', args=[self.slug])

    # Overriding save() method
    # To save an object back to the database, call save():
    def save(self, *args, **kwargs):
        # Converts a string to a URL slug
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
