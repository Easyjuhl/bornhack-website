# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-08 17:47


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("program", "0007_auto_20160807_1333")]

    operations = [
        migrations.AlterModelOptions(name="event", options={"ordering": ["title"]}),
        migrations.AlterModelOptions(name="speaker", options={"ordering": ["name"]}),
        migrations.AddField(
            model_name="speaker",
            name="slug",
            field=models.SlugField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="event",
            name="days",
            field=models.ManyToManyField(blank=True, null=True, to="camps.Day"),
        ),
        migrations.AlterField(
            model_name="event",
            name="end",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="start",
            field=models.TimeField(blank=True, null=True),
        ),
    ]
