# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created')),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=1, max_length=1, null=True, blank=True, choices=[(1, b'Active'), (0, b'Inactive')])),
                ('closed', models.DateTimeField(null=True, verbose_name=b'Date Closed', blank=True)),
                ('name', models.CharField(max_length=75)),
                ('object_id', models.PositiveIntegerField(help_text=b'The record id from another table.', null=True, blank=True)),
                ('type_of_test', models.CharField(max_length=75, choices=[(b'200 Test', b'200 Test')])),
                ('urlorfield', models.CharField(help_text=b'A URL or field name containing the url in the related object', max_length=1000, verbose_name=b'Url or Field Name')),
                ('group', models.CharField(max_length=75, choices=[(b'Apps', b'Apps'), (b'Data Layers', b'Data Layers'), (b'Services', b'Services')])),
                ('table', models.ForeignKey(blank=True, to='contenttypes.ContentType', help_text=b'Use this to pull a link dynamically from another table.', null=True)),
            ],
            options={
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestRun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tests', models.ManyToManyField(to='heartbeat.Test')),
            ],
        ),
        migrations.CreateModel(
            name='TestRunResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created')),
                ('result', models.CharField(max_length=75, choices=[(b'ISSUE', b'ISSUE'), (b'OK', b'OK')])),
                ('latency', models.DecimalField(help_text=b'Response time in milliseconds', max_digits=15, decimal_places=3)),
                ('response', models.TextField(null=True, blank=True)),
                ('test', models.ForeignKey(to='heartbeat.Test')),
                ('test_run', models.ForeignKey(blank=True, to='heartbeat.TestRun', null=True)),
            ],
            options={
                'ordering': ['-created', 'test'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='test',
            unique_together=set([('table', 'object_id', 'type_of_test', 'urlorfield')]),
        ),
    ]
