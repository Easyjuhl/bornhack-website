# Generated by Django 2.0.4 on 2018-05-12 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("program", "0050_auto_20180512_1650")]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="track",
            field=models.ForeignKey(
                help_text="The track this event belongs to",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="events",
                to="program.EventTrack",
            ),
        ),
        migrations.AlterField(
            model_name="eventproposal",
            name="track",
            field=models.ForeignKey(
                help_text="The track this event belongs to",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="eventproposals",
                to="program.EventTrack",
            ),
        ),
    ]
