# Generated by Django 3.2.14 on 2023-02-15 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20221124_1639'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infoloop',
            options={'ordering': ['-updated']},
        ),
        migrations.RemoveField(
            model_name='infoloop',
            name='start_all_exchanges',
        ),
        migrations.RemoveField(
            model_name='infoloop',
            name='start_banks_exchanges',
        ),
        migrations.RemoveField(
            model_name='infoloop',
            name='start_crypto_exchanges',
        ),
        migrations.AddField(
            model_name='infoloop',
            name='count_of_rates',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]