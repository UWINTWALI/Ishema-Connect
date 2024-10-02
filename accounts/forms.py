
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, SetPasswordForm






# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['bio', 'skills', 'interests', 'profile_picture', 'role']
#         widgets = {
#             'bio': forms.Textarea(attrs={'placeholder': 'Tell us about yourself', 'rows': 3}),
#             'skills': forms.TextInput(attrs={'placeholder': 'Your skills'}),
#             'interests': forms.TextInput(attrs={'placeholder': 'Your interests'}),
#             'profile_picture': forms.FileInput(),
#             'role': forms.Select(choices=UserProfile.USER_ROLE_CHOICES),
#         }
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'skills', 'interests', 'profile_picture', 'role']
        widgets = {
            'bio': forms.Textarea(attrs={
                'placeholder': 'Share a bit about yourself',
                'rows': 4,
                'class': 'form-control rounded',
                'style': 'resize:none;'
            }),
            'skills': forms.TextInput(attrs={
                'placeholder': 'Enter your skills',
                'class': 'form-control rounded'
            }),
            'interests': forms.TextInput(attrs={
                'placeholder': 'List your interests',
                'class': 'form-control rounded'
            }),
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-control-file'
            }),
            'role': forms.Select(attrs={
                'class': 'form-select rounded'
            }),
        }
        labels = {
            'bio': 'About You',
            'skills': 'Your Skills',
            'interests': 'Your Interests',
            'profile_picture': 'Profile Picture',
            'role': 'Role',
        }



class LoginForm(AuthenticationForm):
    """Customized login form with styles for username and password fields."""
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'placeholder': 'Username',
            'class': 'form-control',
            'style': 'border: 1px solid #007bff; padding: 10px; border-radius: 5px;',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
            'style': 'border: 1px solid #007bff; padding: 10px; border-radius: 5px;',
        })
    )




class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=UserProfile.USER_ROLE_CHOICES)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            UserProfile.objects.create(user=user, role=self.cleaned_data['role'])
        return user
    

class SignUpForm(UserCreationForm):
     email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
     first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
     last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))



     class Meta:
            model = User
            fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

            def __init__(self, *args, **kwargs):
                 super(SignUpForm, self).__init__(*args, **kwargs)
                 self.fields['username'].widget.attrs['class'] = 'form-control'
                 self.fields['username'].widget.attrs['placeholder'] = 'User Name'
                 self.fields['username'].label = ''
                 self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

                 self.fields['password1'].widget.attrs['class'] = 'form-control'
                 self.fields['password1'].widget.attrs['placeholder'] = 'Password'
                 self.fields['password1'].label = ''
                 self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

                 self.fields['password2'].widget.attrs['class'] = 'form-control'
                 self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
                 self.fields['password2'].label = ''
                 self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'



class UserInfoForm(forms.ModelForm):
    bio = forms.CharField(
        label="", 
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type bio'}),
        required=False
    )
    skills = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'List skills'}),
        required=False
    )
    interests = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Interest'}),
        required=False
    )
    profile_picture = forms.ImageField(
        label="Edit Profile Picture", 
        required=False
    )
    role = forms.ChoiceField(
        choices=UserProfile.USER_ROLE_CHOICES, 
        label="Select Your Role", 
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select role'}),
        required=False
    )

    class Meta:
        model = UserProfile
        fields = ('bio', 'skills', 'interests', 'profile_picture', 'role')
