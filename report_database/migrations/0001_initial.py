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
            name='Folder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('folder_name', models.CharField(default='Unnamed', unique=True, max_length=50)),
                ('private', models.BooleanField(default=False)),
                ('uniqueid', models.CharField(blank=True, unique=True, default=uuid.uuid4, null=True, max_length=100)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='folder_creator')),
                ('shared_users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('report_name', models.CharField(default='Unnamed', max_length=50)),
                ('date', models.DateField()),
                ('sdesc', models.CharField(max_length=60)),
                ('ldesc', models.CharField(max_length=1000)),
                ('private', models.BooleanField(default=False)),
                ('f1n', models.CharField(blank=True, null=True, max_length=50)),
                ('file_1', models.FileField(blank=True, null=True, upload_to='documents')),
                ('encrypt_1', models.BooleanField(default=False)),
                ('f2n', models.CharField(blank=True, null=True, max_length=50)),
                ('file_2', models.FileField(blank=True, null=True, upload_to='documents')),
                ('encrypt_2', models.BooleanField(default=False)),
                ('f3n', models.CharField(blank=True, null=True, max_length=50)),
                ('file_3', models.FileField(blank=True, null=True, upload_to='documents')),
                ('encrypt_3', models.BooleanField(default=False)),
                ('delete_report', models.BooleanField(default=False)),
                ('uniqueid', models.CharField(blank=True, unique=True, default=uuid.uuid4, null=True, max_length=100)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='report_creator')),
                ('folder', models.ForeignKey(blank=True, to='report_database.Folder', null=True, related_name='Folder')),
            ],
        ),
    ]
