# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 15:52
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("shop", "0038_auto_20170323_2021")]

    operations = [
        migrations.AddField(
            model_name="coinifyapicallback",
            name="body",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="coinifyapicallback",
            name="payload",
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
