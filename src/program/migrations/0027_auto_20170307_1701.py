# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 16:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("camps", "0019_auto_20170131_1849"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("program", "0026_speaker_user"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="speaker",
            unique_together=set([("camp", "user"), ("camp", "slug"), ("camp", "name")]),
        )
    ]
