# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-07 19:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eschool', '0004_auto_20170903_1725'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('A', 'Absent'), ('P', 'Present')], max_length=1)),
                ('reason_of_absence', models.TextField()),
                ('student_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eschool.Student')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.CharField(max_length=50)),
                ('subject_ID', models.CharField(max_length=50)),
                ('Total_Mark', models.IntegerField()),
                ('comment', models.TextField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('name', models.CharField(default='simplicio', max_length=200)),
                ('surname', models.CharField(default='sithole', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Continuous_Assessment',
            fields=[
                ('marks_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teachers.Marks')),
                ('Test_name', models.CharField(max_length=50)),
                ('Test_mark', models.IntegerField(null=True)),
            ],
            bases=('teachers.marks',),
        ),
        migrations.CreateModel(
            name='ExamMark',
            fields=[
                ('marks_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teachers.Marks')),
                ('paper1_Mark', models.IntegerField(blank=True, null=True)),
                ('paper2_Mark', models.IntegerField(blank=True, null=True)),
                ('paper3_Mark', models.IntegerField(blank=True, null=True)),
                ('paper4_Mark', models.IntegerField(blank=True, null=True)),
                ('paper5_Mark', models.IntegerField(blank=True, null=True)),
                ('paper6_Mark', models.IntegerField(blank=True, null=True)),
            ],
            bases=('teachers.marks',),
        ),
        migrations.AddField(
            model_name='marks',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]