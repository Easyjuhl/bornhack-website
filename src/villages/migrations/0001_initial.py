# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-05 21:38


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("camps", "0005_auto_20160510_2011"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Village",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(blank=True, max_length=255)),
                ("description", models.TextField()),
                (
                    "open",
                    models.BooleanField(
                        default=False,
                        help_text="Is this village open for others to join?",
                    ),
                ),
                (
                    "camp",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="camps.Camp"
                    ),
                ),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["name"]},
        )
    ]
