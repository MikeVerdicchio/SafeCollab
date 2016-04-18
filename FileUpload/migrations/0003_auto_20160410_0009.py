# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FileUpload', '0002_auto_20160410_0008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='docfile',
            new_name='mocfile',
        ),
    ]
