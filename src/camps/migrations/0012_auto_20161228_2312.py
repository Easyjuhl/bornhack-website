# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 23:12


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("camps", "0011_auto_20161228_1750")]

    operations = [
        migrations.RemoveField(model_name="camp", name="logo_large"),
        migrations.RemoveField(model_name="camp", name="logo_small"),
    ]
