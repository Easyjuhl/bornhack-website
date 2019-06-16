# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 21:49


import django.contrib.postgres.fields.ranges
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("program", "0010_auto_20161212_1809")]

    operations = [
        migrations.AlterModelOptions(
            name="eventinstance", options={"ordering": ["when"]}
        ),
        migrations.RemoveField(model_name="eventinstance", name="end"),
        migrations.RemoveField(model_name="eventinstance", name="start"),
        migrations.AddField(
            model_name="eventinstance",
            name="when",
            field=django.contrib.postgres.fields.ranges.DateTimeRangeField(null=True),
        ),
    ]
