# Generated by Django 5.0.1 on 2024-02-05 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_userprofile_is_verified_alter_userprofile_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='verification_code',
            field=models.IntegerField(default=111111, max_length=6),
        ),
    ]
