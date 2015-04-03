# This technical data was produced for the U. S. Government under Contract No. W15P7T-13-C-F600, and
# is subject to the Rights in Technical Data-Noncommercial Items clause at DFARS 252.227-7013 (FEB 2012)

from django.forms import ModelForm
from .models import Report, Actions, Billet


class ReportForm(ModelForm):
    class Meta:
        model = Report
        exclude = ('owner', 'rating_count')


class ReportFormMinimal(ModelForm):
    class Meta:
        model = Report
        exclude = ('owner', 'content_type', 'object_id')


class ActionForm(ModelForm):
    class Meta:
        model = Actions
        exclude = ('owner', 'rating_count')


class BilletForm(ModelForm):
    class Meta:
        model = Billet
        fields = [
            'name',
            'date_open',
            'date_advertised',
            'date_filled',
            'date_start',
            'date_expires',
            'date_vacant',
            'date_extension',
            'date_review',
            'date_selected',
            'dept',
            'org',
            'status',
            'band_level',
            'selectee',
            'comments',
            'aon_id',
            'tags',
        ]
