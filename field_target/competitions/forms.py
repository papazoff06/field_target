from django import forms
from django.forms import modelformset_factory
from .models import Competition, Registration


class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class CompetitionCreationForm(CompetitionForm):
    class Meta:
        model = Competition
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }


class CompetitionEditForm(CompetitionForm):
    class Meta:
        model = Competition
        fields = '__all__'


class CompetitionRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['accommodation']
        widgets = {
            'accommodation': forms.Select(attrs={'class': 'form-control'}),
        }

class ScoreUpdateForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['first_day_score', 'second_day_score', 'tird_day_score']

