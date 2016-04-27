# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('report_database', '0008_auto_20160426_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='report_creator'),
        ),
    ]
