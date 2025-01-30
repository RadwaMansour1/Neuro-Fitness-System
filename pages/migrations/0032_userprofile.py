# Generated by Django 5.0.1 on 2024-02-07 20:04

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0031_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=128)),
                ('level', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Beginner', max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('verification_code', models.CharField(default='', max_length=6, validators=[django.core.validators.MaxLengthValidator(limit_value=6)])),
                ('registration_method', models.CharField(choices=[('Default', 'Default'), ('Google', 'Google'), ('Facebook', 'Facebook')], default='Default', max_length=100)),
            ],
        ),
    ]
