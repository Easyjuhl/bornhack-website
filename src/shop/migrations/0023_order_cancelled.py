# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 08:53


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("shop", "0022_auto_20160530_2301")]

    operations = [
        migrations.AddField(
            model_name="order",
            name="cancelled",
            field=models.BooleanField(default=False),
        )
    ]
