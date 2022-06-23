# Generated by Django 4.0.4 on 2022-06-21 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_remove_guide_id_team_guide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='guide',
        ),
        migrations.AddField(
            model_name='team',
            name='guide',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.guide'),
        ),
    ]
