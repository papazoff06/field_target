from django import forms
from .models import Competition, Registration

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['name', 'date', 'location', 'description']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['competition', 'accommodation']
