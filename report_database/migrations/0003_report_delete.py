# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_database', '0002_auto_20160412_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='delete',
            field=models.BooleanField(default=False),
        ),
    ]
