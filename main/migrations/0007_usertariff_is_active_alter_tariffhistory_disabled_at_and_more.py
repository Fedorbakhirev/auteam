# Generated by Django 4.0 on 2021-12-22 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_usertariff_enabled_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertariff',
            name='is_active',
            field=models.BooleanField(default=0, verbose_name='Активный'),
        ),
        migrations.AlterField(
            model_name='tariffhistory',
            name='disabled_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата отключения'),
        ),
        migrations.AlterField(
            model_name='usertariff',
            name='enabled_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата активации'),
        ),
    ]
