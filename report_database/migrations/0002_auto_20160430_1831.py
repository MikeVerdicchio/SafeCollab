# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='f1n',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='f2n',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='f3n',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
