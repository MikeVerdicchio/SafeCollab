# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_messages', '0003_message_encrypt'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='encrypt_pw',
            field=models.CharField(verbose_name='Encrypt PW', default='', max_length=120),
        ),
    ]
