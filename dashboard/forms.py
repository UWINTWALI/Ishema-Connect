from django import forms
from opportunities.models import Organization 

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'description', 'contact_info', 'website', 'location']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter organization name',
                'required': 'required',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your organization...',
                'rows': 4,
                'required': 'required',
            }),
            'contact_info': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contact information (e.g., phone, email)',
                'required': 'required',
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Website (optional)',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Location (e.g., city, state)',
                'required': 'required',
            }),
        }
