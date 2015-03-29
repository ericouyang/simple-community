# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='degree',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
