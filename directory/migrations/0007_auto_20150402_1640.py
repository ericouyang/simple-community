# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0006_auto_20150402_1635'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ('-class_year',)},
        ),
    ]
