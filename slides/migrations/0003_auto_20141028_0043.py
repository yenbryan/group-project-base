# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0002_slide_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='day',
            field=models.CharField(max_length=150),
            preserve_default=True,
        ),
    ]
