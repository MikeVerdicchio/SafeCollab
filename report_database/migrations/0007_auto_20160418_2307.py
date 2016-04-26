# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('report_database', '0006_auto_20160418_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='uniqueid',
            field=models.CharField(blank=True, null=True, default=uuid.uuid4, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_name',
            field=models.CharField(default='Unnamed', max_length=50),
        ),
    ]
