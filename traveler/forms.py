from django import forms
from .models import Traveler


class TravelerForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = ['nickname', 'email', 'country']
        widgets = {
            'nickname': forms.TextInput(attrs={
                'placeholder': 'Enter a unique nickname...',
                'aria-describedby': 'id_nickname_helptext',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter a valid email address...',
            }),
            'country': forms.TextInput(attrs={
                'placeholder': 'Enter a country code like <BGR>...',
            }),
        }
        help_texts = {
            'nickname': '*Nicknames can contain only letters and digits.',
        }
        labels = {
            'nickname': 'Nickname:',
            'email': 'Email:',
            'country': 'Country:',
        }


class TravelerEditForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = ['nickname', 'email', 'country', 'about_me']
        widgets = {
            'about_me': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
        }
        help_texts = {
            'nickname': '*Nicknames can contain only letters and digits.',
        }
