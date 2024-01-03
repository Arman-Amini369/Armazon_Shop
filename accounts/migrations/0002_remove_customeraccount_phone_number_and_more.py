# Generated by Django 5.0 on 2024-01-02 09:22

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeraccount',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='customeraccount',
            name='username',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IR', unique=True),
        ),
    ]