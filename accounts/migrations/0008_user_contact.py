# Generated by Django 2.2.8 on 2020-08-14 17:25

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_user_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contact',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]