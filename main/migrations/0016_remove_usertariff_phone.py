# Generated by Django 4.0 on 2021-12-24 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_usertariff_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertariff',
            name='phone',
        ),
    ]
