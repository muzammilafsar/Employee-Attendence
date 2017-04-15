# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 18:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20170414_2354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time_in',
            field=models.TimeField(default=datetime.time(23, 56, 16, 164990)),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time_out',
            field=models.TimeField(default=datetime.time(23, 56, 16, 164990)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
