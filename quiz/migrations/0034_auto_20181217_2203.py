# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-17 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0033_auto_20181217_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_solved',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_solved',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]