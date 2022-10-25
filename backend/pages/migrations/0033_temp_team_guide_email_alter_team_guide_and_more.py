# Generated by Django 4.0.4 on 2022-07-08 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0032_team_reg_no_3_team_student_3_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='temp_team',
            name='guide_email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='guide',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='guide_email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='no_of_members',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=10),
        ),
        migrations.AlterField(
            model_name='temp_team',
            name='guide',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='temp_team',
            name='no_of_members',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=10),
        ),
    ]