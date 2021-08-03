# Generated by Django 3.2.5 on 2021-08-03 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tickets", "0020_populate_ticket_used_when"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discountticket",
            name="used_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="shopticket",
            name="used_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="sponsorticket",
            name="used_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
