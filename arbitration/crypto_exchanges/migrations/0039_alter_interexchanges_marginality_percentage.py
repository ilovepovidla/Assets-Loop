# Generated by Django 3.2.14 on 2022-11-19 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_exchanges', '0038_alter_interexchanges_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interexchanges',
            name='marginality_percentage',
            field=models.FloatField(verbose_name='Marginality percentage'),
        ),
    ]
