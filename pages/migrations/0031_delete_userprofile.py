# Generated by Django 5.0.1 on 2024-02-07 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_history_user'),
        ('pages', '0030_customuser_is_active'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
