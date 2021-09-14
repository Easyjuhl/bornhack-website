# Generated by Django 3.2.7 on 2021-09-14 08:34

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("economy", "0027_zettlebalance_zettlereceipt"),
    ]

    operations = [
        migrations.CreateModel(
            name="MobilePayTransaction",
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
                (
                    "event",
                    models.CharField(
                        help_text="The type of MobilePay transaction", max_length=100
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        help_text="The currency of this transaction.", max_length=3
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The amount of this transaction",
                        max_digits=12,
                    ),
                ),
                (
                    "mobilepay_created",
                    models.DateTimeField(
                        help_text="The MobilePay date and time for this transaction."
                    ),
                ),
                (
                    "comment",
                    models.CharField(
                        blank=True,
                        help_text="The description of this transaction. Rarely used when MobilePay is used through Zettle.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "transaction_id",
                    models.CharField(
                        blank=True,
                        help_text="The transaction id. Can be empty if the type of transaction is a transfer (bank payout).",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "transfer_id",
                    models.CharField(
                        blank=True,
                        help_text="The ID of the transfer (payout) this transaction was included in. Can be empty if this transaction has not yet been included in a transfer.",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "payment_point",
                    models.CharField(
                        help_text="The payment point. For now we only have one (which we rename from year to year)",
                        max_length=100,
                    ),
                ),
                (
                    "myshop_number",
                    models.IntegerField(
                        help_text="The MobilePay MyShop number for this payment. For now we only have one."
                    ),
                ),
                (
                    "bank_account",
                    models.CharField(
                        blank=True,
                        help_text="The bank account this transaction was transferred to. Can be empty if this is a payment (sale) which has not yet been included in a transfer.",
                        max_length=100,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
