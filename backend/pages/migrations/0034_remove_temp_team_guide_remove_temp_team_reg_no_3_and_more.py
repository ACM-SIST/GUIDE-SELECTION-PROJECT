# Generated by Django 4.0.4 on 2022-10-10 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0033_temp_team_guide_email_alter_team_guide_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temp_team',
            name='guide',
        ),
        migrations.RemoveField(
            model_name='temp_team',
            name='reg_no_3',
        ),
        migrations.RemoveField(
            model_name='temp_team',
            name='student_3_email',
        ),
        migrations.RemoveField(
            model_name='temp_team',
            name='student_3_name',
        ),
        migrations.RemoveField(
            model_name='temp_team',
            name='student_3_no',
        ),
    ]
