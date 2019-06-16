# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-12 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("teams", "0040_auto_20180412_2109")]

    operations = [
        migrations.RemoveField(model_name="teammember", name="irc_channel_acl_ok"),
        migrations.AddField(
            model_name="teammember",
            name="irc_acl_fix_needed",
            field=models.BooleanField(
                default=False,
                help_text="Maintained by the IRC bot, manual editing should not be needed. Will be set to true when a teammember sets or changes NickServ username, and back to false after the ACL has been fixed by the bot.",
            ),
        ),
    ]
