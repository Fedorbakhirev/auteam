# Generated by Django 4.0 on 2021-12-25 12:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0017_usertariff_phone_number_alter_usertariff_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariffhistory',
            name='engineer',
            field=models.ForeignKey(blank=True, limit_choices_to={'groups__name': 'Инженер'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Обработал', to='auth.user', verbose_name='Инженер'),
        ),
        migrations.AlterField(
            model_name='usertariff',
            name='phone_number',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть в формате: '+79992345679'", regex='^(\\+7|7|8)?[\\s\\-]?\\(?[489][0-9]{2}\\)?[\\s\\-]?[0-9]{3}[\\s\\-]?[0-9]{2}[\\s\\-]?[0-9]{2}$')], verbose_name='Номер телефона'),
        ),
    ]
