# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-12 11:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_auto_20180205_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.date(2018, 2, 12)),
        ),
    ]