# Generated by Django 4.1.2 on 2022-11-04 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_productcategory_product_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
    ]
