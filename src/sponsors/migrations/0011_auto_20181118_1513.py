# Generated by Django 2.1.2 on 2018-11-18 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0010_populate_logo_filename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='logo',
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='logo_filename',
            field=models.CharField(help_text='Filename of the logo', max_length=255),
        ),
    ]