from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'category', 'image_description', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-b', 'placeholder': 'Enter a title'}),
            'category': forms.TextInput(attrs={'class': 'form-control-b', 'placeholder': 'Enter a category'}),
            'image_description': forms.Textarea(attrs={'class': 'form-control-b', 'placeholder': 'Enter a brief description'}),
        }


