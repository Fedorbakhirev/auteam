# Generated by Django 4.0 on 2021-12-26 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_remove_contact_user_contact_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
    ]
