# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_database', '0005_auto_20160418_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_name',
            field=models.CharField(unique=True, default='Unnamed', max_length=50),
        ),
    ]
