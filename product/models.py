from django.db import models
from django.core.validators import *
from django.urls import reverse


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ], default=0)
    summary = models.CharField(max_length=350, null=True)
    is_active = models.BooleanField(default=False)

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
        return reverse('product.show', args=[self.id])
