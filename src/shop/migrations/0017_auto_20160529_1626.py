# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-29 16:26


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("shop", "0016_auto_20160529_1122")]

    operations = [
        migrations.AlterModelOptions(name="order", options={"ordering": ["-created"]})
    ]
