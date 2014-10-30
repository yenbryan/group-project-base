# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0002_auto_20141028_2338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='action',
            old_name='timed',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='timed',
            new_name='time',
        ),
    ]
