# Generated by Django 3.2.14 on 2022-08-06 23:07

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0001_Add_New'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntraBanksNotLoopedExchangesUpdates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Update date')),
                ('duration', models.DurationField(default=datetime.timedelta(0))),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_exchanges_not_looped', to='banks.banks')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IntraBanksNotLoopedExchanges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_of_transfers', models.JSONField()),
                ('marginality_percentage', models.FloatField(blank=True, default=None, null=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_exchanges_not_looped_update', to='banks.banks')),
                ('update', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datas', to='banks.intrabanksnotloopedexchangesupdates')),
            ],
        ),
    ]