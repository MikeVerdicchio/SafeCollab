# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('report_name', models.CharField(max_length=50, default='Unnamed')),
                ('date', models.DateField()),
                ('sdesc', models.CharField(max_length=60)),
                ('ldesc', models.CharField(max_length=1000)),
                ('private', models.BooleanField(default=False)),
                ('file_1', models.FileField(blank=True, null=True, upload_to='documents')),
                ('encrypt_1', models.BooleanField(default=False)),
                ('file_2', models.FileField(blank=True, null=True, upload_to='documents')),
                ('encrypt_2', models.BooleanField(default=False)),
                ('file_3', models.FileField(blank=True, null=True, upload_to='documents')),
                ('encrypt_3', models.BooleanField(default=False)),
                ('delete_report', models.BooleanField(default=False)),
                ('uniqueid', models.CharField(max_length=100, null=True, unique=True, blank=True, default=uuid.uuid4)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
