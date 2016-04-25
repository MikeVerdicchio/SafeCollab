# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('subject', models.CharField(max_length=120, verbose_name='Subject')),
                ('body', models.TextField(verbose_name='Body')),
                ('sent_at', models.DateTimeField(null=True, verbose_name='sent at', blank=True)),
                ('read_at', models.DateTimeField(null=True, verbose_name='read at', blank=True)),
                ('replied_at', models.DateTimeField(null=True, verbose_name='replied at', blank=True)),
                ('sender_deleted_at', models.DateTimeField(null=True, verbose_name='Sender deleted at', blank=True)),
                ('recipient_deleted_at', models.DateTimeField(null=True, verbose_name='Recipient deleted at', blank=True)),
                ('encrypt', models.BooleanField(default=False, verbose_name='Encrypt')),
                ('parent_msg', models.ForeignKey(verbose_name='Parent message', blank=True, to='django_messages.Message', null=True, related_name='next_messages')),
                ('recipient', models.ForeignKey(verbose_name='Recipient', blank=True, to=settings.AUTH_USER_MODEL, null=True, related_name='received_messages')),
                ('sender', models.ForeignKey(verbose_name='Sender', blank=True, to=settings.AUTH_USER_MODEL, null=True, related_name='sent_messages')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'ordering': ['-sent_at'],
            },
        ),
    ]
