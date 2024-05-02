from django import forms
from .models import Skill

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'proficiency']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'proficiency': forms.NumberInput(attrs={'type': 'range', 'min': 0, 'max': 100, 'step': 1, 'class': 'form-range'}),
        }
