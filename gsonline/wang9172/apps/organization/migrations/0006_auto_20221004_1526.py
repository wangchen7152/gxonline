# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2022-10-04 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20221003_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='points',
            field=models.CharField(blank=True, max_length=128, verbose_name='\u6559\u5b66\u7279\u70b9'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='year',
            field=models.IntegerField(default=66, max_length=64, verbose_name='\u5e74\u9f84'),
        ),
    ]