# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
import tinymce.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('url', models.URLField(max_length=600, null=True, blank=True)),
                ('logo', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Agencies',
            },
        ),
        migrations.CreateModel(
            name='Deployment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deployment_location', models.CharField(max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created')),
                ('closed', models.DateTimeField(null=True, verbose_name=b'Date Closed', blank=True)),
                ('description', tinymce.models.HTMLField(max_length=1000, null=True, blank=True)),
                ('status', models.IntegerField(default=1, max_length=1, choices=[(1, b'Active'), (0, b'Inactive')])),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('deployers', models.ManyToManyField(max_length=250, null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Event name.', max_length=200)),
                ('tags', models.CharField(max_length=75, null=True, blank=True)),
                ('event_type', models.CharField(max_length=50, choices=[(b'Avalanche', b'Avalanche'), (b'Hurricane/Cyclone', b'Hurricane_Cyclone'), (b'Tornado', b'Tornado'), (b'Earthquake', b'Earthquake'), (b'Extreme Weather', b'Extreme Weather'), (b'Fire', b'Fire'), (b'Flood', b'Flood'), (b'Tsunami', b'Tsunami'), (b'Volcano', b'Volcano'), (b'Pandemic', b'Pandemic'), (b'Special Event', b'Special Event'), (b'Exercise', b'Exercise')])),
                ('posture', models.CharField(default=b'Monitoring', max_length=25, choices=[(b'Monitoring', b'Monitoring'), (b'Collecting', b'Collecting'), (b'Reporting', b'Reporting'), (b'Deployed', b'Deployed')])),
                ('status', models.IntegerField(default=1, max_length=1, choices=[(1, b'Active'), (0, b'Inactive')])),
                ('event_location', models.CharField(help_text=b'A human-friendly description of the location (ie Japan, or Pacific Ocean)', max_length=200, null=True)),
                ('closed', models.DateTimeField(null=True, verbose_name=b"Date Event is marked 'Closed', or no longer active", blank=True)),
                ('description', tinymce.models.HTMLField(help_text=b'A generic description of the event, markdown is enabled.', max_length=1000, null=True, verbose_name=b'Overview', blank=True)),
                ('poc', tinymce.models.HTMLField(help_text=b'Point of Contact for the event.', max_length=1000, null=True, blank=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('link', models.URLField(help_text=b'This is an auto-generated link/slug to link to the event.', null=True, blank=True)),
                ('collaboration_link', models.URLField(default=b'', null=True, blank=True)),
                ('product_feed_url', models.TextField(help_text=b'URL for any Non-standard products to be pulled for this event. If empty, will pull based on event name and tags.', null=True, blank=True)),
                ('standard_product_url', models.TextField(help_text=b'Link to Standard Products for this incident. Will merge with Non-standard feed.', max_length=800, null=True, blank=True)),
                ('rfi_generator_id', models.PositiveIntegerField(help_text=b'RFI Generator ID for this incident. Leave empty for none.', null=True, blank=True)),
                ('filedropoff_path', models.CharField(help_text=b'Advanced - Path to folder within AjaxExplorer Shared directory of files to show - must be in /cache/ajaxplorer/files', max_length=200, null=True, blank=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('slug', models.SlugField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created')),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('show_event_on_map', models.BooleanField(default=True, help_text=b'Choose whether the incident icon should show up on the map.')),
                ('show_timeline', models.BooleanField(default=True, help_text=b'Choose whether the timeline should be enabled for the event.')),
                ('show_services', models.BooleanField(default=True, help_text=b'Choose whether to show services associated with an event.')),
                ('show_notes', models.BooleanField(default=True, help_text=b'Choose whether to show notes associated with an event.')),
                ('show_products', models.BooleanField(default=True, help_text=b'Choose whether to show products associated with an event.')),
                ('show_rfis', models.BooleanField(default=True, help_text=b'Choose whether to show RFIs associated with an event.')),
                ('show_deployments', models.BooleanField(default=True, help_text=b'Choose whether to show deployments associated with an event.')),
                ('show_supporting_agencies', models.BooleanField(default=True, help_text=b'Choose whether to show supporting agencies.')),
                ('show_geomedia_triage', models.BooleanField(default=True, help_text=b'Choose whether to show a page to filter social media.')),
                ('show_related_files', models.BooleanField(default=True, help_text=b'Choose whether to show files saved in the dropbox.')),
                ('show_supporting_apps', models.BooleanField(default=True, help_text=b'Choose whether to show the supporting apps section.')),
                ('agencies', models.ManyToManyField(help_text=b'Adds each agencies logo to the event page.', to='operations.Agency', null=True, blank=True)),
            ],
            options={
                'ordering': ['-last_updated'],
            },
        ),
        migrations.CreateModel(
            name='GeoWidget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'GeoLink widget name', unique=True, max_length=200)),
                ('url', models.TextField(help_text=b'Template for the url to lookup, i.e. http://api.geonames.org/wikipediaBoundingBoxJSON?formatted=true&north={{n}}&south={{s}}', null=True, blank=True)),
                ('url_if_local', models.CharField(help_text=b'Template for the url to use if testing locally', max_length=100, null=True, blank=True)),
                ('description', models.CharField(max_length=300, null=True, blank=True)),
                ('type', models.CharField(max_length=50, choices=[(b'List', b'List')])),
                ('below_zoom', models.PositiveIntegerField(help_text=b'Show this widget only when map is below this zoom level.', null=True, blank=True)),
                ('above_zoom', models.PositiveIntegerField(help_text=b'Show this widget only when map is above this zoom level.', null=True, blank=True)),
                ('listName', models.CharField(help_text=b'Name of array that data is returned in', max_length=100, null=True, blank=True)),
                ('tabToOpenIn', models.CharField(default=b'_new', max_length=20, null=True, help_text=b'Name of a window/tab to open in', blank=True)),
                ('selectorName', models.TextField(help_text=b'Template of where to find the name of each returned item, i.e. {{title}}', null=True, blank=True)),
                ('selectorLink', models.TextField(help_text=b'Template of where to find where results should link to, i.e. http://{{wikipediaUrl}}', null=True, blank=True)),
                ('selectorPoint', models.TextField(help_text=b"Template of where to find the 'lat long' of each returned item, i.e. {{lat}} {{lng}}", null=True, blank=True)),
                ('selectorSummary', models.TextField(help_text=b'Template of where to find the summary of each returned item, i.e. {{summary}}', null=True, blank=True)),
                ('selectorShowIf', models.TextField(help_text=b'Template of what to run, and only show if results are true. i.e. {{settings.type==3}}', null=True, blank=True)),
                ('style', models.TextField(help_text=b"CSS style object of results. i.e. {'color':'blue','fontSize':'10px'}", null=True, blank=True)),
                ('data_type', models.CharField(max_length=20, choices=[(b'json', b'json'), (b'xml', b'xml')])),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'geolink',
                'verbose_name_plural': 'GeoLink Page Lookup Widgets',
            },
        ),
        migrations.CreateModel(
            name='LessonLearned',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created')),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=1, max_length=1, null=True, blank=True, choices=[(1, b'Active'), (0, b'Inactive')])),
                ('closed', models.DateTimeField(null=True, verbose_name=b'Date Closed', blank=True)),
                ('name', models.CharField(max_length=200, null=True, verbose_name=b'Title', blank=True)),
                ('due', models.DateTimeField(null=True, verbose_name=b'Resolution Due By', blank=True)),
                ('priority', models.CharField(default=b'Low', max_length=25, null=True, blank=True, choices=[(b'Low', b'Low'), (b'Medium', b'Medium'), (b'High', b'High')])),
                ('description', tinymce.models.HTMLField(max_length=1000, null=True)),
                ('work_around', tinymce.models.HTMLField(max_length=1000, null=True, blank=True)),
                ('action', tinymce.models.HTMLField(max_length=1000, null=True, blank=True)),
                ('resolution', tinymce.models.HTMLField(max_length=1000, null=True, blank=True)),
                ('assigned_to', models.ForeignKey(related_name='lesson_learned_assignment', blank=True, to=settings.AUTH_USER_MODEL, max_length=250, null=True)),
            ],
            options={
                'ordering': ['-created'],
                'abstract': False,
                'verbose_name_plural': 'Lessons Learned',
            },
        ),
        migrations.CreateModel(
            name='LessonLearnedCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', tinymce.models.HTMLField(max_length=1000, null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Lessons Learned Categories',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75)),
                ('description', tinymce.models.HTMLField(max_length=800, null=True, blank=True)),
                ('url', models.URLField(max_length=600)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=1, max_length=1, choices=[(1, b'Active'), (0, b'Inactive')])),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'resource',
                'verbose_name_plural': 'resources',
            },
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('description', tinymce.models.HTMLField(max_length=800, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=1, max_length=1, choices=[(1, b'Active'), (0, b'Inactive')])),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'resource type',
                'verbose_name_plural': 'resource types',
            },
        ),
        migrations.CreateModel(
            name='SitRep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created')),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.IntegerField(default=1, max_length=1, null=True, blank=True, choices=[(1, b'Active'), (0, b'Inactive')])),
                ('closed', models.DateTimeField(null=True, verbose_name=b'Date Closed', blank=True)),
                ('name', models.CharField(max_length=200, null=True, verbose_name=b'Title', blank=True)),
                ('content', tinymce.models.HTMLField(help_text=b'Content of sitrep markdown is enabled.', max_length=6000)),
                ('event', models.ForeignKey(blank=True, to='operations.Event', null=True)),
                ('owner', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, max_length=250, null=True)),
            ],
            options={
                'ordering': ['-created'],
                'abstract': False,
                'verbose_name_plural': 'SitReps',
            },
        ),
        migrations.AddField(
            model_name='service',
            name='service_type',
            field=models.ManyToManyField(to='operations.ServiceType'),
        ),
        migrations.AddField(
            model_name='lessonlearned',
            name='category',
            field=models.ForeignKey(blank=True, to='operations.LessonLearnedCategory', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lessonlearned',
            name='event',
            field=models.ForeignKey(blank=True, to='operations.Event', null=True),
        ),
        migrations.AddField(
            model_name='lessonlearned',
            name='submitted_by',
            field=models.ForeignKey(related_name='lesson_learned_submission', blank=True, to=settings.AUTH_USER_MODEL, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='geowidgets',
            field=models.ManyToManyField(help_text=b'Related GeoWidgets', to='operations.GeoWidget', null=True, verbose_name=b'geowidgets', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='map',
            field=models.ForeignKey(blank=True, to='maps.Map', help_text=b'Choose a map for the event.', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='services',
            field=models.ManyToManyField(help_text=b'Related Resources to show on side of page', to='operations.Service', null=True, verbose_name=b'resources', blank=True),
        ),
        migrations.AddField(
            model_name='deployment',
            name='event',
            field=models.ForeignKey(to='operations.Event'),
        ),
        migrations.AlterUniqueTogether(
            name='lessonlearned',
            unique_together=set([('submitted_by', 'description', 'event')]),
        ),
    ]
