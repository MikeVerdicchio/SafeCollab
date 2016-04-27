# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_messages', '0004_message_encrypt_pw'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='decrypt_pw',
            field=models.CharField(max_length=120, verbose_name='Decrypt PW', default=''),
        ),
    ]
