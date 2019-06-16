# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-09 10:00


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("shop", "0030_auto_20160827_0752")]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="payment_method",
            field=models.CharField(
                choices=[
                    (b"credit_card", b"Credit card"),
                    (b"blockchain", b"Blockchain"),
                    (b"bank_transfer", b"Bank transfer"),
                    (b"cash", b"Cash"),
                ],
                default=b"",
                max_length=50,
            ),
        )
    ]
