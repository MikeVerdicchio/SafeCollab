# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FileUpload', '0003_auto_20160410_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='mocfile',
            new_name='docfile',
        ),
    ]
