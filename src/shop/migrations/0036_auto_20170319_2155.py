# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("shop", "0035_auto_20170222_1629")]

    operations = [
        migrations.AlterField(
            model_name="product", name="slug", field=models.SlugField(unique=True)
        )
    ]
