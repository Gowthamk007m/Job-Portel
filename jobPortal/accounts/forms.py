from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, PasswordInput, CharField
from django.core.validators import MinLengthValidator
from .models import *
from django.contrib.auth import password_validation

class UserCreation(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']
        widgets = {
            'email': TextInput({
            'class': 'form-control mt-4' ,
            'type':'email',
            'id':'Email1',
            'aria-describedby':'emailHelp',
            'placeholder':'Enter email'
            }),
            'password1': PasswordInput({
                'class': 'form-control mt-4',
                'placeholder':'Enter Password'
            }),
               'password2': PasswordInput({
                'class': 'form-control mt-4',
                'placeholder':'Enter Password'
            }),
        }   
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        password_validation.validate_password(password2, self.instance)
        return password2
    
    
class UsersignUpForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=("Password"),
        widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control mt-4'}),)
    password2 = forms.CharField(label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'form-control mt-4'}),
        help_text=("Enter the same password as above, for verification."))

    class Meta:
        model = CustomUser
        fields = ("email",)

        widgets = {
            'email': TextInput({
            'class': 'form-control mt-4',
            'type':'email',
            'id':'Email1',
            'aria-describedby':'emailHelp',
            'placeholder':'Enter email'
            })}

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
    