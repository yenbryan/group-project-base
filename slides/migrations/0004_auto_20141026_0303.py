# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def create_initial_student_base(apps, schema_editor):
    Profile = apps.get_model('slides','Profile')

    for i in range(25):
        Profile.objects.create(username='student{}'.format(i),
            password="test",
            email='student{}@test.com'.format(i),
            first_name='first{}'.format(i),
            last_name='last{}'.format(i),
            image='profile_pictures/default-profile-photo.png')

class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0002_auto_20141026_0028'),
    ]

    operations = [
        migrations.RunPython(create_initial_student_base)
    ]
