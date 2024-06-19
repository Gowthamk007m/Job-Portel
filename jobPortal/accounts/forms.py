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
    
    
class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6)
    
class EmailForm(forms.Form):
    email = forms.EmailField()

class OTPFormReset(forms.Form):
    otp = forms.CharField(max_length=6)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")