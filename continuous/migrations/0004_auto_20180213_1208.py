# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-13 10:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('continuous', '0003_auto_20180205_1101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='continuous_assessment',
            old_name='subject_ID',
            new_name='subject_name',
        ),
    ]
