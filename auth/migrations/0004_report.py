# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthConfig', '0003_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField()),
                ('sdesc', models.CharField(max_length=60)),
                ('ldesc', models.CharField(max_length=1000)),
                ('private', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(to='AuthConfig.User')),
            ],
        ),
    ]
