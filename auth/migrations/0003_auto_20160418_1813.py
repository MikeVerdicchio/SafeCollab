# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthConfig', '0002_auto_20160418_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='public_key',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
