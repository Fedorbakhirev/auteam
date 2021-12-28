# Generated by Django 4.0 on 2021-12-23 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0011_tariffhistory_desc_tariffhistory_is_canceled_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usertariff',
            options={'verbose_name': 'Тариф пользователя', 'verbose_name_plural': 'Тариф пользователя'},
        ),
        migrations.RenameField(
            model_name='tariffhistory',
            old_name='is_canceled',
            new_name='is_declined',
        ),
        migrations.AlterField(
            model_name='complaint',
            name='engineer',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'Инженер'}, on_delete=django.db.models.deletion.CASCADE, related_name='Инженер', to='auth.user', verbose_name='Инженер'),
        ),
    ]
