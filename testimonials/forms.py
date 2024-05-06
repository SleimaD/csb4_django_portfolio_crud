from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['first_name', 'last_name', 'position', 'text', 'image']  

        
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control-d','cols': 40, 'rows': 3}),
            'first_name': forms.TextInput(attrs={'class': 'form-control-d','placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control-d','placeholder': 'Enter last name'}),
            'position': forms.TextInput(attrs={'class': 'form-control-d','placeholder': 'Enter position'}),
            
        }

        labels = {
            'text': 'Testimonial Text',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'position': 'Position'
        }