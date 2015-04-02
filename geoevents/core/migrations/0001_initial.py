# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageLinks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Name of site-wide variable', max_length=50)),
                ('category', models.CharField(help_text=b'Category on header bar that link should go under, will create a new one if needed', max_length=100, null=True, blank=True)),
                ('url', models.TextField(help_text=b"URL to page loaded in new tab. If a 'shortcut' is specified, add URL onto end of internal url (e.g. '?service=SuggestionBox')", max_length=800, null=True, blank=True)),
                ('shortcut', models.CharField(help_text=b"Internal shortcut to use instead of url (e.g. 'add-feedback')", max_length=100, null=True, blank=True)),
                ('show_for_types', models.CharField(help_text=b"Leave blank to always show, or use 'incident' or 'dashboard' or something to only show in pages that have that in the url", max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Name of site-wide variable', max_length=200)),
                ('value', models.TextField(help_text=b'Value of site-wide variable', max_length=800, blank=True)),
            ],
        ),
    ]
