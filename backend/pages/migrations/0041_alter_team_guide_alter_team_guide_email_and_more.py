# Generated by Django 4.0.4 on 2023-01-27 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0040_alter_guide_email_alter_team_project_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='guide',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='guide_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='reg_no_1',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='student_1_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='student_1_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='student_1_no',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
