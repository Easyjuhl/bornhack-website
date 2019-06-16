# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-18 13:18
from __future__ import unicode_literals

from django.db import migrations


def create_eventtypes(apps, schema_editor):
    Type = apps.get_model("events", "Type")
    Type.objects.create(name="public_credit_name_changed")


class Migration(migrations.Migration):

    dependencies = [("events", "0001_initial")]

    operations = [migrations.RunPython(create_eventtypes)]
