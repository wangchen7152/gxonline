# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2022-10-03 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20221002_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default=1, max_length=256, upload_to='course/%Y/%m', verbose_name='\u5934\u50cf'),
            preserve_default=False,
        ),
    ]