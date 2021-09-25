# Generated by Django 3.2.7 on 2021-09-25 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("economy", "0029_bankaccount_help_texts"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coinifyinvoice",
            name="original_payment_id",
            field=models.IntegerField(
                blank=True,
                help_text="The original payment id (used when the invoice payment type is extra)",
                null=True,
            ),
        ),
    ]
