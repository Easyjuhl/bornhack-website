# Generated by Django 2.0.4 on 2018-05-21 21:55

from django.db import migrations


def add_urltypes(apps, schema_editor):
    UrlType = apps.get_model("program", "UrlType")

    UrlType.objects.create(name="Other", icon="link")

    UrlType.objects.create(name="Homepage", icon="link")

    UrlType.objects.create(name="Slides", icon="link")

    UrlType.objects.create(name="Twitter", icon="link")

    UrlType.objects.create(name="Mastodon", icon="link")

    UrlType.objects.create(name="Facebook", icon="link")

    UrlType.objects.create(name="Project", icon="link")

    UrlType.objects.create(name="Blog", icon="link")


class Migration(migrations.Migration):

    dependencies = [("program", "0055_auto_20180521_2354")]

    operations = [migrations.RunPython(add_urltypes)]
