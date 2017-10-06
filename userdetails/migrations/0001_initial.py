# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size_Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Length', models.IntegerField(blank=True, null=True)),
                ('UK', models.IntegerField(blank=True, null=True)),
                ('EU', models.IntegerField(blank=True, null=True)),
                ('Length_ID', models.IntegerField(blank=True, null=True)),
                ('Gender', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
