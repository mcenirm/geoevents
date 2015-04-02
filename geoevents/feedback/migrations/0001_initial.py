# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200)),
                ('active', models.BooleanField(default=True, help_text=b'Uncheck to hide FAQ.')),
                ('common_issue', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created')),
                ('content', tinymce.models.HTMLField(null=True, blank=True)),
                ('slug', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=75)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('organization', models.CharField(max_length=25, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created')),
                ('subject', models.CharField(default=b'Geo Event Page', max_length=25, choices=[(b'Suggestion Box', b'Suggestion Box'), (b'Landing Page', b'Landing Page'), (b'Geo Event Page', b'Geo Event Page'), (b'Press Page', b'http://www.yourserver.com/contact')])),
                ('login_method', models.CharField(default=b'CAC', max_length=25, choices=[(b'CAC Card', b'CAC Card'), (b'Name/PW Account', b'Name/PW Account'), (b'PKI', b'PKI'), (b'No Name/PW', b'No Name/PW')])),
                ('platform', models.CharField(default=b'CAC', max_length=25, choices=[(b'Desktop', b'Desktop'), (b'Mobile', b'Mobile'), (b'Other', b'Other')])),
                ('feedback', models.TextField(max_length=1000)),
                ('referer', models.TextField(max_length=200, null=True, blank=True)),
                ('user_agent', models.TextField(max_length=300, null=True, blank=True)),
                ('phone', models.CharField(max_length=12, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
        migrations.CreateModel(
            name='SubjectEmailMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(help_text=b'For feedback emails, which ones should go to an alternate email list? Enter Subject exactly as is in pulldown menu', unique=True, max_length=75)),
                ('emails', models.TextField(help_text=b'Comma-separated list of emails that should be used instead of defaults', max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='feedback.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='last_updated_by',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
