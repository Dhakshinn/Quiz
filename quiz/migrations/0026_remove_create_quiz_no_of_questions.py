# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-04 11:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0025_question_view_title_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='create_quiz',
            name='no_of_questions',
        ),
    ]
