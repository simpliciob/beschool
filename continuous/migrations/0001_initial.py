# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-07 23:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Continuous_Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.CharField(max_length=50)),
                ('subject_ID', models.CharField(max_length=50)),
                ('Total_Mark', models.IntegerField()),
                ('comment', models.TextField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('name', models.CharField(default='simplicio', max_length=200)),
                ('surname', models.CharField(default='sithole', max_length=40)),
                ('Test_name', models.CharField(max_length=50)),
                ('Test_mark', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]