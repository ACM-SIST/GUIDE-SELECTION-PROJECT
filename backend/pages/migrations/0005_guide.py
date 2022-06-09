# Generated by Django 4.0.4 on 2022-06-07 08:52

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_delete_guide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('domain_1', models.CharField(max_length=200)),
                ('domain_2', models.CharField(blank=True, max_length=200)),
                ('domain_3', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('experience', models.IntegerField()),
                ('myImage', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('vacancy', models.IntegerField(default=7)),
            ],
        ),
    ]
