# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_database', '0004_auto_20160418_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='encrypt_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='report',
            name='encrypt_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='report',
            name='encrypt_3',
            field=models.BooleanField(default=False),
        ),
    ]
