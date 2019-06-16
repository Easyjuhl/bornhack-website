# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 17:50


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("camps", "0010_auto_20161220_1714")]

    operations = [
        migrations.AddField(
            model_name="camp",
            name="logo_large",
            field=models.CharField(
                default="",
                help_text=b"The filename of the large logo to use on the frontpage of this camp",
                max_length=100,
                verbose_name=b"Large logo for this camp",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="camp",
            name="logo_small",
            field=models.CharField(
                default="",
                help_text=b"The filename of the small logo to use in the top of the page for this camp",
                max_length=100,
                verbose_name=b"Small logo for this camp",
            ),
            preserve_default=False,
        ),
    ]
