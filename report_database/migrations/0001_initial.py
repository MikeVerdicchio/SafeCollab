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
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('folder_name', models.CharField(default='Unnamed', unique=True, max_length=50)),
                ('private', models.BooleanField(default=False)),
                ('uniqueid', models.CharField(default=uuid.uuid4, unique=True, null=True, blank=True, max_length=100)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='folder_creator')),
                ('shared_users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('report_name', models.CharField(default='Unnamed', max_length=50)),
                ('date', models.DateField()),
                ('sdesc', models.CharField(max_length=60)),
                ('ldesc', models.CharField(max_length=1000)),
                ('private', models.BooleanField(default=False)),
                ('f1n', models.CharField(default='', null=True, blank=True, max_length=50)),
                ('file_1', models.FileField(null=True, blank=True, upload_to='documents')),
                ('encrypt_1', models.BooleanField(default=False)),
                ('f2n', models.CharField(default='', null=True, blank=True, max_length=50)),
                ('file_2', models.FileField(null=True, blank=True, upload_to='documents')),
                ('encrypt_2', models.BooleanField(default=False)),
                ('f3n', models.CharField(default='', null=True, blank=True, max_length=50)),
                ('file_3', models.FileField(null=True, blank=True, upload_to='documents')),
                ('encrypt_3', models.BooleanField(default=False)),
                ('delete_report', models.BooleanField(default=False)),
                ('uniqueid', models.CharField(default=uuid.uuid4, unique=True, null=True, blank=True, max_length=100)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='report_creator')),
                ('folder', models.ForeignKey(related_name='Folder', blank=True, null=True, to='report_database.Folder')),
            ],
        ),
    ]
