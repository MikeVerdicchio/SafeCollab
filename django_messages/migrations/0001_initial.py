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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('subject', models.CharField(verbose_name='Subject', max_length=120)),
                ('body', models.TextField(verbose_name='Body')),
                ('sent_at', models.DateTimeField(blank=True, verbose_name='sent at', null=True)),
                ('read_at', models.DateTimeField(blank=True, verbose_name='read at', null=True)),
                ('replied_at', models.DateTimeField(blank=True, verbose_name='replied at', null=True)),
                ('sender_deleted_at', models.DateTimeField(blank=True, verbose_name='Sender deleted at', null=True)),
                ('recipient_deleted_at', models.DateTimeField(blank=True, verbose_name='Recipient deleted at', null=True)),
                ('encrypt', models.BooleanField(default=False, verbose_name='Encrypt')),
                ('encrypt_message', models.BinaryField(default='', verbose_name='Encrypt Body')),
                ('decrypt_pw', models.TextField(default='', verbose_name='Decrypt PW')),
                ('parent_msg', models.ForeignKey(verbose_name='Parent message', to='django_messages.Message', related_name='next_messages', blank=True, null=True)),
                ('recipient', models.ForeignKey(verbose_name='Recipient', to=settings.AUTH_USER_MODEL, related_name='received_messages', blank=True, null=True)),
                ('sender', models.ForeignKey(verbose_name='Sender', to=settings.AUTH_USER_MODEL, related_name='sent_messages', blank=True, null=True)),
            ],
            options={
                'ordering': ['-sent_at'],
                'verbose_name_plural': 'Messages',
                'verbose_name': 'Message',
            },
        ),
    ]
