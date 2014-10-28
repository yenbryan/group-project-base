# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0002_auto_20141028_0202'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='slide',
            unique_together=set([('week', 'day', 'am_pm', 'slide_number', 'name')]),
        ),
    ]
