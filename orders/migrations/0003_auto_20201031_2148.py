# Generated by Django 2.2.8 on 2020-10-31 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Address',
            new_name='address',
        ),
    ]