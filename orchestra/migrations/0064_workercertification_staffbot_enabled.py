# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orchestra', '0063_worker_staffing_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='workercertification',
            name='staffbot_enabled',
            field=models.BooleanField(default=True),
        ),
    ]
