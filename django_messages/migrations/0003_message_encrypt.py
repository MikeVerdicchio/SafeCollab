# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_messages', '0002_auto_20160331_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='encrypt',
            field=models.BooleanField(default=False, verbose_name='Encrypt'),
        ),
    ]
