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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('subject', models.CharField(max_length=120, verbose_name='Subject')),
                ('body', models.TextField(verbose_name='Body')),
                ('sent_at', models.DateTimeField(null=True, blank=True, verbose_name='sent at')),
                ('read_at', models.DateTimeField(null=True, blank=True, verbose_name='read at')),
                ('replied_at', models.DateTimeField(null=True, blank=True, verbose_name='replied at')),
                ('sender_deleted_at', models.DateTimeField(null=True, blank=True, verbose_name='Sender deleted at')),
                ('recipient_deleted_at', models.DateTimeField(null=True, blank=True, verbose_name='Recipient deleted at')),
                ('encrypt', models.BooleanField(default=False, verbose_name='Encrypt')),
                ('encrypt_pw', models.CharField(max_length=120, default='', verbose_name='Encrypt PW')),
                ('decrypt_pw', models.CharField(max_length=120, default='', verbose_name='Decrypt PW')),
                ('parent_msg', models.ForeignKey(null=True, to='django_messages.Message', verbose_name='Parent message', related_name='next_messages', blank=True)),
                ('recipient', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, verbose_name='Recipient', related_name='received_messages', blank=True)),
                ('sender', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, verbose_name='Sender', related_name='sent_messages', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Messages',
                'ordering': ['-sent_at'],
                'verbose_name': 'Message',
            },
        ),
    ]
