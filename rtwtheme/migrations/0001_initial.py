# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-27 09:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('heading', models.CharField(help_text='The heading under the icon blurbs', max_length=200)),
                ('subheading', models.CharField(help_text='The subheading just below the heading', max_length=200)),
            ],
            options={
                'verbose_name': 'Home page',
                'verbose_name_plural': 'Home pages',
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolios',
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('image', mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='Image')),
                ('homepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slides', to='rtwtheme.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
    ]
