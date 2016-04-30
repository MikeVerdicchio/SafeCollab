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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('subject', models.CharField(max_length=120, verbose_name='Subject')),
                ('body', models.TextField(verbose_name='Body')),
                ('sent_at', models.DateTimeField(null=True, blank=True, verbose_name='sent at')),
                ('read_at', models.DateTimeField(null=True, blank=True, verbose_name='read at')),
                ('replied_at', models.DateTimeField(null=True, blank=True, verbose_name='replied at')),
                ('sender_deleted_at', models.DateTimeField(null=True, blank=True, verbose_name='Sender deleted at')),
                ('recipient_deleted_at', models.DateTimeField(null=True, blank=True, verbose_name='Recipient deleted at')),
                ('encrypt', models.BooleanField(default=False, verbose_name='Encrypt')),
                ('encrypt_message', models.BinaryField(default='', verbose_name='Encrypt Body')),
                ('decrypt_pw', models.TextField(default='', verbose_name='Decrypt PW')),
                ('parent_msg', models.ForeignKey(null=True, blank=True, verbose_name='Parent message', to='django_messages.Message', related_name='next_messages')),
                ('recipient', models.ForeignKey(null=True, blank=True, verbose_name='Recipient', to=settings.AUTH_USER_MODEL, related_name='received_messages')),
                ('sender', models.ForeignKey(null=True, blank=True, verbose_name='Sender', to=settings.AUTH_USER_MODEL, related_name='sent_messages')),
            ],
            options={
                'verbose_name_plural': 'Messages',
                'verbose_name': 'Message',
                'ordering': ['-sent_at'],
            },
        ),
    ]
