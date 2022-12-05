# Generated by Django 4.1.2 on 2022-11-12 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='ایجاد شده'),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='ویرایش شده'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='ایجاد شده'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='ویرایش شده'),
        ),
        migrations.AddField(
            model_name='producttag',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='ایجاد شده'),
        ),
        migrations.AddField(
            model_name='producttag',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='ویرایش شده'),
        ),
    ]