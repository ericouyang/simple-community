# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0004_auto_20150402_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='town_city',
            field=models.CharField(max_length=50, verbose_name=b'Town/City', blank=True),
            preserve_default=True,
        ),
    ]
