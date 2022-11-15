# Generated by Django 4.1.2 on 2022-11-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('email', models.CharField(max_length=300, verbose_name='ایمیل')),
                ('full_name', models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')),
                ('message', models.TextField(verbose_name='متن تماس با ما')),
                ('response', models.TextField(blank=True, null=True, verbose_name='پاسخ تماس با ما')),
                ('is_read_by_admin', models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='ویرایش شده')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'لیست تماس با ما',
            },
        ),
    ]
