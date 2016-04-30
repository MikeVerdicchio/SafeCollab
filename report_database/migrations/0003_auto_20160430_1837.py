# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report_database', '0002_auto_20160430_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('docfile', models.FileField(blank=True, null=True, upload_to='documents')),
                ('encrypt', models.BooleanField(default=False)),
                ('private', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='report',
            name='encrypt_1',
        ),
        migrations.RemoveField(
            model_name='report',
            name='encrypt_2',
        ),
        migrations.RemoveField(
            model_name='report',
            name='encrypt_3',
        ),
        migrations.RemoveField(
            model_name='report',
            name='f1n',
        ),
        migrations.RemoveField(
            model_name='report',
            name='f2n',
        ),
        migrations.RemoveField(
            model_name='report',
            name='f3n',
        ),
        migrations.RemoveField(
            model_name='report',
            name='file_1',
        ),
        migrations.RemoveField(
            model_name='report',
            name='file_2',
        ),
        migrations.RemoveField(
            model_name='report',
            name='file_3',
        ),
        migrations.AddField(
            model_name='documents',
            name='report',
            field=models.ForeignKey(related_name='report', to='report_database.Report'),
        ),
        migrations.AddField(
            model_name='documents',
            name='shared_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
