# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wth', '0003_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measure',
            name='location',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='measures', to='wth.Location'),
        ),
    ]
