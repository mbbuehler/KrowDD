# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-23 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0003_auto_20170223_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='ig',
            field=models.FloatField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='feature',
            name='p',
            field=models.FloatField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='feature',
            name='p_0',
            field=models.FloatField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='feature',
            name='p_1',
            field=models.FloatField(blank=True, default=None),
        ),
    ]
