# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-05 07:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190305_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grade',
            old_name='user_id',
            new_name='user',
        ),
    ]
