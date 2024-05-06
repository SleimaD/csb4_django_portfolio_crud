from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'icon', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-c', 'placeholder': 'Enter a title'}),
            'icon': forms.Select(attrs={'class': 'form-select', 'placeholder': 'select an icon'}),
            'description': forms.Textarea(attrs={'class': 'form-controldes', 'placeholder': 'Enter a brief description...'}),
        }

