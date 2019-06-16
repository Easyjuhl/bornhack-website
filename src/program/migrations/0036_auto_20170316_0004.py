# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 23:04
from __future__ import unicode_literals

from django.db import migrations, models
import program.models


class Migration(migrations.Migration):

    dependencies = [("program", "0035_auto_20170314_2325")]

    operations = [
        migrations.AlterField(
            model_name="speakerproposal",
            name="picture_large",
            field=models.ImageField(
                blank=True,
                help_text="A picture of the speaker",
                max_length=255,
                null=True,
                storage=program.models.CustomUrlStorage(),
                upload_to=program.models.get_speakerproposal_picture_upload_path,
            ),
        ),
        migrations.AlterField(
            model_name="speakerproposal",
            name="picture_small",
            field=models.ImageField(
                blank=True,
                help_text="A thumbnail of the speaker picture",
                max_length=255,
                null=True,
                storage=program.models.CustomUrlStorage(),
                upload_to=program.models.get_speakerproposal_picture_upload_path,
            ),
        ),
    ]
