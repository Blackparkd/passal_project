from django import forms
from .models import Event, Location

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'name',       
            'category',
            'start_date',
            'end_date',
            'expense',
            'location',
            'artists',      
            'notes'
        ]
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'artists': forms.CheckboxSelectMultiple(),
        }

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            'name',
            'country',     
            'city',        
            'street',
            'zip_code',
            'capacity',
            'notes'
        ]