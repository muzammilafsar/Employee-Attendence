# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 19:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20170414_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='Absent',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.date(2017, 4, 15)),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time_in',
            field=models.TimeField(default=datetime.time(0, 50, 48, 413250)),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time_out',
            field=models.TimeField(default=datetime.time(0, 50, 48, 413250)),
        ),
    ]
