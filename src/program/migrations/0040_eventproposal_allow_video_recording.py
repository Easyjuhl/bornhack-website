# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-09 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("program", "0039_auto_20170430_1408")]

    operations = [
        migrations.AddField(
            model_name="eventproposal",
            name="allow_video_recording",
            field=models.BooleanField(
                default=False, help_text="If we can video record the event or not"
            ),
        )
    ]
