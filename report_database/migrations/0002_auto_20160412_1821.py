# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_database', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='uploadFile',
            new_name='file_1',
        ),
        migrations.AddField(
            model_name='report',
            name='file_2',
            field=models.FileField(upload_to='documents', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='file_3',
            field=models.FileField(upload_to='documents', blank=True, null=True),
        ),
    ]
