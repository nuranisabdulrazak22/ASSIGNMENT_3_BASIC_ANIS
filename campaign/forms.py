from django import apps
from django import forms
from .models import Volunteer

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'email', 'interest']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'interest': forms.Select(attrs={'class': 'form-select'}),
        }