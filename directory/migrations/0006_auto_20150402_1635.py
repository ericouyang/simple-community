# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0005_auto_20150402_1619'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ('class_year',)},
        ),
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ('type',)},
        ),
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ('name',)},
        ),
    ]
