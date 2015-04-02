# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=75, choices=[(b'ArcGIS93Rest', b'ArcGIS93Rest'), (b'WMS', b'WMS'), (b'KML', b'KML'), (b'GeoRSS', b'GeoRSS'), (b'GeoJSON', b'GeoJSON'), (b'GPX', b'GPX'), (b'GML', b'GML'), (b'WMTS', b'WMTS'), (b'MapBox', b'MapBox'), (b'TileServer', b'TileServer'), (b'GetCapabilities', b'GetCapabilities')])),
                ('url', models.URLField(help_text=b'URL of service. If WMS, can be any valid URL. Otherwise, the URL will require a local proxy and Firewall change to access it', max_length=600)),
                ('layer', models.CharField(help_text=b'The layer name from the GetCapabilities document. Many ESRI servers have just "0" or "1" for layers names. Layer names can sometimes be comma-separated ("0,1,2"), and are not needed for data layers such as KML, GeoRSS, GeoJSON..', max_length=800, null=True, blank=True)),
                ('image_format', models.CharField(blank=True, max_length=75, null=True, help_text=b'The MIME type of the image format to use for tiles on WMS layers (image/png, image/jpeg image/gif...). Double check that the server exposes this exactly - some servers push png instead of image/png.', choices=[(b'image/png', b'image/png'), (b'image/png8', b'image/png8'), (b'image/jpeg', b'image/jpeg'), (b'image/gif', b'image/gif'), (b'image/tiff', b'image/tiff'), (b'image/tiff8', b'image/tiff8'), (b'image/geotiff', b'image/geotiff'), (b'image/geotiff8', b'image/geotiff8'), (b'image/svg', b'image/svg'), (b'rss', b'rss'), (b'kml', b'kml'), (b'kmz', b'kmz'), (b'json', b'json'), (b'png', b'png'), (b'png8', b'png8'), (b'jpeg', b'jpeg'), (b'jpg', b'jpg'), (b'gif', b'gif'), (b'tiff', b'tiff'), (b'tiff8', b'tiff8'), (b'geotiff', b'geotiff'), (b'geotiff8', b'geotiff8'), (b'svg', b'svg')])),
                ('description', models.TextField(help_text=b'Text to show in layer chooser, please be descriptive - this will soon be searchable', max_length=800, null=True, blank=True)),
                ('attribution', models.CharField(help_text=b'Attribution from layers to the map display (will show in bottom of map when layer is visible).', max_length=200, null=True, blank=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True, help_text=b'Categories that will be used to organize map layers that users can add to map from the Layers button', choices=[(b'Disease', b'Disease'), (b'Earthquakes', b'Earthquakes'), (b'Event-Specific', b'Event-Specific'), (b'Fires', b'Fires'), (b'Floods', b'Floods'), (b'Human Geography', b'Human Geography'), (b'Hurricanes', b'Hurricanes'), (b'Infrastructure', b'Infrastructure'), (b'Tsunami', b'Tsunami'), (b'Volcanoes', b'Volcanoes')])),
                ('styles', models.CharField(help_text=b'The name of a style to use for this layer (only useful for WMS layers if the server exposes it.)', max_length=200, null=True, blank=True)),
                ('transparent', models.BooleanField(default=True, help_text=b'If WMS or overlay, should the tiles be transparent where possible?')),
                ('refreshrate', models.PositiveIntegerField(help_text=b'Layer refresh rate in seconds for vector/data layers (will not refresh WMS layers)', null=True, verbose_name=b'Layer Refresh Rate', blank=True)),
                ('token', models.CharField(help_text=b'Authentication token, if required (usually only for secure layer servers)', max_length=400, null=True, blank=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('show_in_table', models.BooleanField(default=True, help_text=b'Draw a table on the Event Pages with any info found from results.')),
                ('allow_image_modifications', models.BooleanField(default=False, help_text=b'Allow the user to change Brightness, Sharpness, etc on layer - requires that the server can proxy to the source server and thus Firewall might need to be opened.')),
                ('extent', django.contrib.gis.db.models.fields.PolygonField(help_text=b'Extent of the layer.', srid=4326, null=True, blank=True)),
                ('layer_parsing_function', models.CharField(blank=True, max_length=100, null=True, help_text=b'Advanced - The javascript function used to parse a data service (GeoJSON, GeoRSS, KML), needs to be an internally known parser. Contact an admin if you need data parsed in a new way.', choices=[(b'palanterra', b'palanterra'), (b'uscg_ships', b'uscg_ships'), (b'icnet', b'icnet'), (b'dg_wmts_time', b'dg_wmts_time'), (b'geomedia_triaged', b'geomedia_triaged'), (b'harvester_earthquake', b'harvester_earthquake'), (b'harvester_fire', b'harvester_fire'), (b'harvester_tsunami', b'harvester_tsunami'), (b'harvester_flood', b'harvester_flood'), (b'harvester_volcano', b'harvester_volcano'), (b'ima', b'ima')])),
                ('enable_identify', models.BooleanField(default=False, help_text=b'Advanced - Allow user to click map to query layer for details. The map server must support queries for this layer.')),
                ('info_format', models.CharField(blank=True, max_length=75, null=True, help_text=b'Advanced - what format the server returns for an WMS-I query', choices=[(b'application/json', b'application/json'), (b'application/vnd.ogc.wms_xml', b'application/vnd.ogc.wms_xml'), (b'application/xml', b'application/xml'), (b'text/html', b'text/html'), (b'text/plain', b'text/plain')])),
                ('root_field', models.CharField(help_text=b'Advanced - For WMS-I (queryable) layers, the root field returned by server. Leave blank for default (will usually be "FIELDS" in returned XML).', max_length=100, null=True, blank=True)),
                ('fields_to_show', models.CharField(help_text=b'Fields to show when someone uses the identify tool to click on the layer. Leave blank for all.', max_length=200, null=True, blank=True)),
                ('downloadableLink', models.URLField(help_text=b'URL of link to supporting tool (such as a KML document that will be shown as a download button)', max_length=300, null=True, blank=True)),
                ('layer_params', models.TextField(help_text=b'JSON key/value pairs to be sent to the web service.  Use double-quotes around both the key and value for JSON. ex: {"crs":"urn:ogc:def:crs:EPSG::4326"}', null=True, blank=True)),
                ('spatial_reference', models.CharField(default=b'EPSG:4326', max_length=32, null=True, help_text=b'The spatial reference of the service.  Should be in ESPG:XXXX format.', blank=True)),
                ('constraints', models.TextField(null=True, blank=True)),
                ('additional_domains', models.TextField(help_text=b'Semicolon seperated list of additional domains for the layer.', null=True, blank=True)),
                ('min_scale', models.FloatField(null=True, blank=True)),
                ('max_scale', models.FloatField(help_text=b'Not yet implemented - Used for Zoom to Layer operation.', null=True, blank=True)),
                ('source_params', models.TextField(help_text=b'Not yet implemented - Options to pass into layer builder', null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=75)),
                ('description', models.TextField(max_length=800, null=True, blank=True)),
                ('zoom', models.IntegerField(help_text=b'Sets the default zoom level of the map.')),
                ('projection', models.CharField(default=b'EPSG:4326', max_length=32, null=True, help_text=b'Set the default projection for layers added to this map. Note that the projection of the map is usually determined by that of the current baseLayer', blank=True)),
                ('center_x', models.FloatField(default=0.0, help_text=b'Sets the center x coordinate of the map.  Maps on event pages default to the location of the event.')),
                ('center_y', models.FloatField(default=0.0, help_text=b'Sets the center y coordinate of the map.  Maps on event pages default to the location of the event.')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MapLayer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shown', models.BooleanField(default=True)),
                ('stack_order', models.IntegerField()),
                ('opacity', models.FloatField(default=0.8)),
                ('is_base_layer', models.BooleanField(help_text=b'Base Layers are mutually exclusive layers, meaning only one can be enabled at any given time. The currently active base layer determines the available projection (coordinate system) and zoom levels available on the map.')),
                ('display_in_layer_switcher', models.BooleanField()),
                ('layer', models.ForeignKey(related_name='map_layer_set', to='maps.Layer')),
                ('map', models.ForeignKey(related_name='map_set', to='maps.Map')),
            ],
            options={
                'ordering': ['stack_order'],
            },
        ),
    ]
