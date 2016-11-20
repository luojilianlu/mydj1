# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 02:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0006_auto_20161117_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('mobile', models.IntegerField(blank=True, null=True, verbose_name='联系电话')),
                ('relation', models.CharField(blank=True, max_length=10, null=True, verbose_name='关系')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.Student', verbose_name='办理学生')),
            ],
        ),
    ]
