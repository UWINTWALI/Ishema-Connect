from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'image']  # Fields to include in the form
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Share Your Experience...'}),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file custom-file-input',  # Custom class for styling
                'style': 'display:none;'  # Hide the default file input
            }),
        }
