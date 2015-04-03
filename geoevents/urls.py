# This technical data was produced for the U. S. Government under Contract No. W15P7T-13-C-F600, and
# is subject to the Rights in Technical Data-Noncommercial Items clause at DFARS 252.227-7013 (FEB 2012)

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from geoevents.views import UserPermsUpdate
from geoevents.views import UserPermsUpdate
from geoevents.operations.views import service_type, service_types
from django.contrib.auth.views import login
from geoevents.views import logout
from geoevents.operations.views import view_services

admin.autodiscover()

urlpatterns = [
    url(r'^/?', include('geoevents.operations.urls')),
    url(r'^/?$', RedirectView.as_view(url=reverse_lazy('active-incidents'), permanent=True), name='home'),
    url(r'^service-type/(?P<name>[\w]+)/$', service_type, name='view-service-type'),
    url(r'^service-types/$', service_types, name='view-service-types'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^users/(?P<username>[\w\d\.@+-_\'\s]+)/$', UserPermsUpdate.as_view(), name='user-profile'),
    url(r'^notes/', include('geoevents.notes.urls')),
    url(r'^services/$', view_services, name='operations-view-services'),
    url(r'^feedback/', include('geoevents.feedback.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^timeline/', include('geoevents.timeline.urls')),
    url(r'^director/', include('geoevents.director.urls')),
]
