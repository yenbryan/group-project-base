# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='slide',
            unique_together=set([('week', 'day', 'am_pm', 'name')]),
        ),
    ]
