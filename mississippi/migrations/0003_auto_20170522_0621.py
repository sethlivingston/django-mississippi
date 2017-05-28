# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mississippi', '0002_resource_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='available_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='available_until',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
