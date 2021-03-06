# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-29 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='create_quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('no_of_questions', models.IntegerField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
