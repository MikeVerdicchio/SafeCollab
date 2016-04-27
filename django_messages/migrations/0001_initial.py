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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
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
                ('parent_msg', models.ForeignKey(null=True, related_name='next_messages', blank=True, to='django_messages.Message', verbose_name='Parent message')),
                ('recipient', models.ForeignKey(null=True, related_name='received_messages', blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Recipient')),
                ('sender', models.ForeignKey(null=True, related_name='sent_messages', blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Sender')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'ordering': ['-sent_at'],
            },
        ),
    ]
