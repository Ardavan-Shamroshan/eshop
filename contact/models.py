from django.db import models


# Create your models here.

# contact
class ContactUs(models.Model):
    subject = models.CharField(max_length=300, verbose_name="عنوان")
    email = models.CharField(max_length=300, verbose_name="ایمیل")
    full_name = models.CharField(max_length=300, verbose_name="نام و نام خانوادگی")
    message = models.TextField(verbose_name="متن تماس با ما")
    response = models.TextField(null=True, blank=True, verbose_name="پاسخ تماس با ما")
    is_read_by_admin = models.BooleanField(default=False, verbose_name="خوانده شده توسط ادمین")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='ویرایش شده')

    # to display an object in the Django admin site and as the value inserted into a template
    # when it displays an object.
    # Thus, you should always return a nice, human-readable representation of the model
    # from the __str__() method.
    def __str__(self):
        return f"{self.subject}"

    # To override the database table name, use the db_table parameter in class Meta.
    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'


class UserProfile(models.Model):
    image = models.FileField(upload_to='images')
