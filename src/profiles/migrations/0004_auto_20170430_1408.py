# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-30 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("profiles", "0003_auto_20170413_1703")]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="description",
            field=models.TextField(
                blank=True,
                default="",
                help_text="Please include any info you think could be relevant, like drivers license, first aid certificates, crafts, skills and previous experience. Please also include availability if you are not there for the full week.",
            ),
        )
    ]
