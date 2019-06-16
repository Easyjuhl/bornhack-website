# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("program", "0027_auto_20170307_1701")]

    operations = [
        migrations.AddField(
            model_name="event",
            name="submission_status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending approval"),
                    ("approved", "Approved"),
                    ("rejected", "Rejected"),
                ],
                default="pending",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="speaker",
            name="submission_status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending approval"),
                    ("approved", "Approved"),
                    ("rejected", "Rejected"),
                ],
                default="pending",
                max_length=50,
            ),
        ),
    ]
