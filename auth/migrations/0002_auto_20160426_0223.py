# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthConfig', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('site_manager', 'Site Manager'),)},
        ),
        migrations.RemoveField(
            model_name='user',
            name='site_manager',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
