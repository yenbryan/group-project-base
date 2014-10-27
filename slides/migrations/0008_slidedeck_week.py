# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0007_slide_deck'),
    ]

    operations = [
        migrations.AddField(
            model_name='slidedeck',
            name='week',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
