# Generated by Django 5.0.1 on 2024-02-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_alter_userprofile_registration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default='hashed_password_here', max_length=128),
        ),
    ]
