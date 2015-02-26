import os 
 
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'geoevents',
        'USER': 'geoevents',
        'PASSWORD': 'geoevents',
        'HOST': 'db',
        'PORT': 5432,
    }
}

EVENT_FILE_DROPOFF_ROOT = '/tmp/events/'

FILE_UPLOAD_TEMP_DIR = '/tmp/'

FILER_IMAGE_MODEL = False

