# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-05 09:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_auto_20170910_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.date(2018, 2, 5)),
        ),
    ]