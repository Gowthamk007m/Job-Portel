from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .models import *

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control mt-4', 'placeholder': 'First name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control mt-4', 'placeholder': 'Enter email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control mt-4', 'placeholder': 'Password', 'autocomplete': 'off'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control mt-4', 'placeholder': 'Confirm Password', 'autocomplete': 'off'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control mt-4', 'placeholder': 'Lastname'})

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        password_validation.validate_password(password2, self.instance)
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['work_status', 'phone_number', 'contact_email', 'profile_picture', 'resume', 'languages', 'location']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name', 'years_of_exp']

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['certification_name', 'expiration_date']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['level_of_education', 'course_name']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['job_title', 'company_name']