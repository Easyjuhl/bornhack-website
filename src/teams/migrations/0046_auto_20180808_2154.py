# Generated by Django 2.0.4 on 2018-08-08 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("teams", "0045_merge_20180805_1131")]

    operations = [
        migrations.AlterModelOptions(
            name="teamshift", options={"ordering": ("shift_range",)}
        )
    ]
