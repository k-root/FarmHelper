# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 04:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HouseHolds',
            new_name='HouseHold',
        ),
        migrations.RenameModel(
            old_name='Members',
            new_name='Member',
        ),
    ]
