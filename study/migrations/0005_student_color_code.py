# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0004_auto_20161117_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='color_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
