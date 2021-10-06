# Generated by Django 3.2.8 on 2021-10-06 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0052_team_permission_set'),
        ('economy', '0036_auto_20211003_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pos',
            name='team',
            field=models.ForeignKey(help_text='The Team managing this POS', on_delete=django.db.models.deletion.PROTECT, to='teams.team'),
        ),
    ]
