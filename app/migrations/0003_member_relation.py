# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 04:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170830_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='Relation',
            field=models.CharField(default='', max_length=15),
        ),
    ]
