# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 15:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20160725_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjustment',
            name='adjustment_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 25, 0, 4, 49, 331530), verbose_name=b'date adjusted'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_adjustment_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 25, 0, 4, 49, 332430), verbose_name=b'date adjusted'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_adjustment_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='testapp.Adjustment'),
        ),
    ]
