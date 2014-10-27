# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='name',
            field=models.CharField(max_length=150, null=True),
            preserve_default=True,
        ),
    ]