# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='time',
        ),
        migrations.RemoveField(
            model_name='question',
            name='time',
        ),
        migrations.AddField(
            model_name='action',
            name='timed',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 28, 23, 38, 30, 53497, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='timed',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 28, 23, 38, 35, 781111, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
