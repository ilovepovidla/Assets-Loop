# Generated by Django 3.2.14 on 2022-07-18 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parses_p2p', '0005_p2pbinance_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='p2pbinance',
            name='updated',
        ),
    ]
