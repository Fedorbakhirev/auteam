# Generated by Django 4.0 on 2021-12-22 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0007_usertariff_is_active_alter_tariffhistory_disabled_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariffhistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]