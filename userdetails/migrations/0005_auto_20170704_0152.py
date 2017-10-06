# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0004_auto_20170704_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size_chart',
            name='EU',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='size_chart',
            name='Length',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='size_chart',
            name='UK',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
