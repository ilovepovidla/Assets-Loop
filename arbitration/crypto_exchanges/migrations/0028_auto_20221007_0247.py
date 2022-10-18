# Generated by Django 3.2.14 on 2022-10-06 22:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0011_auto_20220930_1426'),
        ('crypto_exchanges', '0027_auto_20221007_0114'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='bestcombinationpaymentchannels',
            name='unique_currency_pair',
        ),
        migrations.AlterField(
            model_name='interbankandcryptoexchanges',
            name='bank_rate',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bank_rate_inter_bank_and_crypro_exchanges', to='banks.bestbankexchanges'),
        ),
        migrations.AddConstraint(
            model_name='bestcombinationpaymentchannels',
            constraint=models.UniqueConstraint(fields=('from_fiat', 'to_fiat', 'input_bank', 'output_bank', 'crypto_exchange'), name='unique_currency_pair'),
        ),
    ]
