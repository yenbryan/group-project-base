# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0006_slidedeck'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='deck',
            field=models.ForeignKey(related_name='slides', default=1, to='slides.SlideDeck'),
            preserve_default=False,
        ),
    ]
