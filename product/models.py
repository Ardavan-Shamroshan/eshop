from django.core.validators import *
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


# product categories (one to many)
class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده / حذف نشده')

    # to display an object in the Django admin site and as the value inserted into a template
    def __str__(self):
        return f"{self.title}"

    # To override the database table name, use the db_table parameter in class Meta.
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


# products
class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ManyToManyField(ProductCategory, related_name='product_categories', verbose_name='دسته بندی ها')
    price = models.IntegerField(verbose_name='قیمت')
    summary = models.CharField(max_length=350, db_index=True, null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True)
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')
    slug = models.SlugField(default='', null=False, blank=True, max_length=200, unique=True)
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده / حذف نشده')

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

    # To override the database table name, use the db_table parameter in class Meta.
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


# product tag
class ProductTag(models.Model):
    caption = models.CharField(max_length=200, db_index=True, verbose_name='تگ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده / حذف نشده')

    # to display an object in the Django admin site and as the value inserted into a template
    def __str__(self):
        return f"{self.caption}"

    # To override the database table name, use the db_table parameter in class Meta.
    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'
