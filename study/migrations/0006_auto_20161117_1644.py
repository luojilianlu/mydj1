# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0005_student_color_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '学生信息', 'verbose_name_plural': '学生信息'},
        ),
        migrations.AlterField(
            model_name='student',
            name='color_code',
            field=models.CharField(default='FF0000', max_length=6, verbose_name='名字颜色'),
        ),
    ]