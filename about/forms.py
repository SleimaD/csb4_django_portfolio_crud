from django import forms
from .models import About

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'subtitle', 'profile_image', 'general_description', 'birthday', 'website', 'phone', 'city', 'age', 'degree', 'email', 'freelance', 'detailed_description']
       
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-a'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control-a'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control-a'}),
            'general_description': forms.Textarea(attrs={'class': 'form-control-a'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control-a', 'type': 'date'}),
            'website': forms.URLInput(attrs={'class': 'form-control-a'}),
            'phone': forms.TextInput(attrs={'class': 'form-control-a'}),
            'city': forms.TextInput(attrs={'class': 'form-control-a'}),
            'age': forms.NumberInput(attrs={'class': 'form-control-a'}),
            'degree': forms.TextInput(attrs={'class': 'form-control-a'}),
            'email': forms.EmailInput(attrs={'class': 'form-control-a'}),
            'freelance_status': forms.Select(attrs={'class': 'form-control-a'}),
            'detailed_description': forms.Textarea(attrs={'class': 'form-control-a'}),
        }
