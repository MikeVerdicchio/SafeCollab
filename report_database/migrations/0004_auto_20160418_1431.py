# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_database', '0003_report_delete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='delete',
            new_name='delete_report',
        ),
    ]
