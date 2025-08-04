from django import forms
from .models import Competition, Registration

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['name', 'start_date', 'end_date', 'location', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'




class CompetitionRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['accommodation']
        widgets = {
            'accommodation': forms.Select(attrs={'class': 'form-control'}),
        }
