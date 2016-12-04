# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtwtheme', '0002_slide_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='heading',
        ),
        migrations.AddField(
            model_name='homepage',
            name='buttontext',
            field=models.CharField(default='Enter', help_text='The text on the button to enter the page', max_length=200),
        ),
        migrations.AddField(
            model_name='homepage',
            name='headline',
            field=models.CharField(default='Switzerland', help_text='The Headline in the middle of the carousel caption', max_length=200),
        ),
        migrations.AddField(
            model_name='homepage',
            name='topheading',
            field=models.CharField(default='We currently are in:', help_text='The top heading of the carousel caption', max_length=200),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='subheading',
            field=models.CharField(blank=True, help_text='The subheading of the carousel caption', max_length=200, null=True),
        ),
    ]
