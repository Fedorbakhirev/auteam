# Generated by Django 4.0 on 2021-12-22 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_usertariff_options_alter_usertariff_tariff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertariff',
            name='enabled_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
