# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('report_name', models.CharField(max_length=50, default='Unnamed')),
                ('date', models.DateField()),
                ('sdesc', models.CharField(max_length=60)),
                ('ldesc', models.CharField(max_length=1000)),
                ('private', models.BooleanField(default=False)),
                ('file_1', models.FileField(null=True, upload_to='documents', blank=True)),
                ('encrypt_1', models.BooleanField(default=False)),
                ('file_2', models.FileField(null=True, upload_to='documents', blank=True)),
                ('encrypt_2', models.BooleanField(default=False)),
                ('file_3', models.FileField(null=True, upload_to='documents', blank=True)),
                ('encrypt_3', models.BooleanField(default=False)),
                ('delete_report', models.BooleanField(default=False)),
                ('uniqueid', models.CharField(null=True, max_length=100, unique=True, blank=True, default=uuid.uuid4)),
                ('creator', models.ForeignKey(related_name='report_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
