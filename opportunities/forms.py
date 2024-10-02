from django import forms
from .models import Opportunity

class OpportunityForm(forms.ModelForm):
    """Form for organizations to input the details of new opportunities"""
    
    class Meta:
        model = Opportunity
        fields = ['opportunity_picture', 'title', 'description', 'location', 'date', 'volunteer_limit']
        
        # Customizing the widgets for styling
        widgets = {
            'opportunity_picture': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #ccc; padding: 10px;',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #007bff; padding: 10px; border-radius: 5px;',
                'placeholder': 'Enter the opportunity title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #007bff; padding: 15px; border-radius: 5px; height: 100px;',
                'placeholder': 'Enter a detailed description',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #007bff; padding: 10px; border-radius: 5px;',
                'placeholder': 'Enter the location',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'style': 'border: 1px solid #007bff; padding: 10px; border-radius: 5px;',
            }),
            'volunteer_limit': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #007bff; padding: 10px; border-radius: 5px;',
                'placeholder': 'Enter volunteer limit',
            }),
        }
