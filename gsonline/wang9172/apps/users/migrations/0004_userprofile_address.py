# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2022-10-06 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220930_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='\u5730\u5740'),
        ),
    ]