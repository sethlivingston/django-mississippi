# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mississippi', '0003_auto_20170522_0621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='views',
        ),
        migrations.AddField(
            model_name='siteresource',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
