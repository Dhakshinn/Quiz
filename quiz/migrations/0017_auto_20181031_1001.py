# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-31 04:31
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0016_auto_20181031_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_solved',
            name='name',
            field=models.CharField(max_length=100, verbose_name=django.contrib.auth.models.User),
        ),
    ]
