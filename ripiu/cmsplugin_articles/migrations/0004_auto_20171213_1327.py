# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-13 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_articles', '0003_auto_20171207_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepluginmodel',
            name='header_alignment',
            field=models.CharField(blank=True, choices=[('left', 'left'), ('right', 'right'), ('center', 'center')], max_length=10, verbose_name='header alignment'),
        ),
        migrations.AddField(
            model_name='sectionpluginmodel',
            name='header_alignment',
            field=models.CharField(blank=True, choices=[('left', 'left'), ('right', 'right'), ('center', 'center')], max_length=10, verbose_name='header alignment'),
        ),
    ]
