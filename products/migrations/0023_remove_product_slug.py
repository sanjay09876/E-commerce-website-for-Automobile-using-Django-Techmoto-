# Generated by Django 2.2.8 on 2020-06-14 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20200614_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
