# Generated by Django 4.0 on 2021-12-24 14:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_usertariff_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertariff',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть в формате: '+79992345679'", regex='^(\\+7|7|8)?[\\s\\-]?\\(?[489][0-9]{2}\\)?[\\s\\-]?[0-9]{3}[\\s\\-]?[0-9]{2}[\\s\\-]?[0-9]{2}$')]),
        ),
        migrations.AlterField(
            model_name='usertariff',
            name='is_paid',
            field=models.DateField(blank=True, null=True, verbose_name='Оплачено до'),
        ),
    ]
