# Generated by Django 4.0 on 2021-12-22 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_usertariff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertariff',
            name='tariff',
        ),
        migrations.AddField(
            model_name='usertariff',
            name='tariff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.tariff'),
        ),
    ]
