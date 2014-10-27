# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0002_auto_20141026_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=b'profile_pictures/default-profile-photo.png', null=True, upload_to=b'profile_pictures', blank=True),
            preserve_default=True,
        ),
    ]
