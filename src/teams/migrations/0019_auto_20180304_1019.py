# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-04 09:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("teams", "0018_auto_20171122_2204")]

    operations = [
        migrations.AlterUniqueTogether(name="team", unique_together=set([])),
        migrations.RemoveField(model_name="team", name="camp"),
    ]
