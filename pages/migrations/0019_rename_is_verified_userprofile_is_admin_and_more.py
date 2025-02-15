# Generated by Django 5.0.1 on 2024-02-05 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_rename_is_staff_userprofile_is_verified_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_verified',
            new_name='is_admin',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='registration_method',
            field=models.CharField(choices=[('Default', 'Default'), ('Google', 'Google'), ('Facebook', 'Facebook')], default='Default', max_length=100),
        ),
    ]
