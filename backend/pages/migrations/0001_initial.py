# Generated by Django 4.0.4 on 2022-06-01 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('domain_1', models.CharField(max_length=20)),
                ('domain_2', models.CharField(max_length=20)),
                ('domain_3', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=29)),
                ('experience', models.IntegerField()),
                ('myImage', models.ImageField(upload_to='photos/%Y/%m/%d')),
            ],
        ),
    ]
