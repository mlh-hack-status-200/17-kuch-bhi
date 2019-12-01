from django import forms
from .models import Med
from django.utils import timezone
from django.contrib import admin
from easy_maps.widgets import AddressWithMapWidget
from .models import Med

class Medform(forms.ModelForm):
    class Meta:
        model = Med
        fields = ('name', 'price', 'phone', 'user_name', 'date', 'address' )
        widgets = {
            'address': AddressWithMapWidget({'class': 'vTextField'})
        }


