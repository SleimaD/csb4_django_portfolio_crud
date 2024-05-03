from django import forms
from .models import About

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'subtitle', 'profile_image', 'general_description', 'birthday', 'website', 'phone', 'city', 'age', 'degree', 'email', 'freelance', 'detailed_description']
       
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
        #     'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
        #     'general_description': forms.Textarea(attrs={'class': 'form-control'}),
        #     'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        #     'website': forms.URLInput(attrs={'class': 'form-control'}),
        #     'phone': forms.TextInput(attrs={'class': 'form-control'}),
        #     'city': forms.TextInput(attrs={'class': 'form-control'}),
        #     'age': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'degree': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'freelance_status': forms.Select(attrs={'class': 'form-control'}),
        #     'detailed_description': forms.Textarea(attrs={'class': 'form-control'}),
        # }
