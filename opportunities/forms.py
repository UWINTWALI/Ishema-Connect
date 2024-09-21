from django import forms
from .models import Opportunity

class OpportunityForm(forms.ModelForm):
    """form for organizations to input the details of new opportunities"""
    class Meta:
        model = Opportunity
        fields = ['opportunity_picture','title', 'description','location', 'date', 'volunteer_limit']
