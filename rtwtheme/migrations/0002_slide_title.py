# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtwtheme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='title',
            field=models.CharField(default='Slide', max_length=50),
        ),
    ]
