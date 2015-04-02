# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimelineItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(help_text=b'Start date in YYYY/MM/DD HH:MM format', verbose_name=b'Start Date')),
                ('end', models.DateTimeField(help_text=b'End date in YYYY/MM/DD HH:MM format', null=True, verbose_name=b'End Date', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created')),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('content', models.CharField(max_length=2000)),
                ('group', models.CharField(max_length=200, null=True, blank=True)),
                ('visible', models.BooleanField(default=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['start'],
                'abstract': False,
            },
        ),
    ]
