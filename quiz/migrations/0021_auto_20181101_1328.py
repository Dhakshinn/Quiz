# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-01 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0020_programming_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='create_quiz',
            name='created_by',
        ),
        migrations.AddField(
            model_name='create_quiz',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
