# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-26 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160801_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='EngineData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(blank=True, max_length=300, null=True)),
                ('appear_time', models.IntegerField()),
            ],
        ),
    ]
