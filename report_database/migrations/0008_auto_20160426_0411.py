# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_database', '0007_auto_20160418_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='creator',
            field=models.ForeignKey(to='AuthConfig.UserProfile'),
        ),
    ]
