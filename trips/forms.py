from django import forms
from .models import Trip


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['destination', 'summary', 'start_date', 'duration', 'image_url']
        widgets = {
            'destination': forms.TextInput(attrs={
                'placeholder': 'Enter a short destination note...',
                'required': True,
                'maxlength': 100
            }),
            'summary': forms.Textarea(attrs={
                'placeholder': 'Share your exciting moments...',
                'rows': 10,
                'cols': 40,
                'required': True
            }),
            'start_date': forms.DateInput(attrs={'type': 'date', 'required': True}),
            'duration': forms.NumberInput(attrs={
                'placeholder': '*Duration in days is expected.',
                'value': 1,
                'min': 1,
                'required': True
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'An optional image URL...',
            }),
        }
        error_messages = {
            'destination': {
                'required': "Please enter a destination.",
            },
            'summary': {
                'required': "Please share a summary.",
            },
            'start_date': {
                'required': "Please select a start date.",
            },
            'duration': {
                'required': "Please specify the duration of the trip.",
                'min_value': "Duration must be at least 1 day.",
            },
        }


class DeleteTripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['destination', 'summary', 'start_date', 'duration', 'image_url']
        widgets = {
            'destination': forms.TextInput(attrs={'readonly': 'readonly'}),
            'summary': forms.Textarea(attrs={'readonly': 'readonly'}),
            'start_date': forms.DateInput(attrs={'readonly': 'readonly'}),
            'duration': forms.NumberInput(attrs={'readonly': 'readonly'}),
            'image_url': forms.URLInput(attrs={'readonly': 'readonly'}),
        }
