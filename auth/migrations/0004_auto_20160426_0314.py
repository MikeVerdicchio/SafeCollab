# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthConfig', '0003_userprofile_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
    ]
