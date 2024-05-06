from django import forms
from .models import ContactInfo
from .models import ContactMessage

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['description', 'street', 'street_number', 'location', 'zipcode', 'email', 'phone']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-controldes', 'placeholder': 'Enter a brief description...'}),
            'street': forms.TextInput(attrs={'class': 'form-controlc', 'placeholder': 'Enter street name'}),
            'street_number': forms.TextInput(attrs={'class': 'form-controlc', 'placeholder': 'Enter street number'}),
            'location': forms.TextInput(attrs={'class': 'form-controlc', 'placeholder': 'Enter location'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-controlc', 'placeholder': 'Enter zipcode'}),
            'email': forms.EmailInput(attrs={'class': 'form-controlc', 'placeholder': 'Enter email address'}),
            'phone': forms.TextInput(attrs={'class': 'form-controlc', 'placeholder': 'Enter phone number'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("This field is required.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone:
            raise forms.ValidationError("This field is required.")
        return phone
    



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
