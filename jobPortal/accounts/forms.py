from django.forms import CharField, ModelForm, PasswordInput, TextInput,Form,Select,CheckboxInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class CustomUserCreationForm(UserCreationForm):
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
            'placeholder':'Enter email',
            'required': 'required'
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
        
class LoginForm(Form):
     email = CharField(
        max_length = 50,
        min_length = 10,
        required = True,
        label = 'email',
        widget = TextInput({
            'class': 'form-control mt-4',
            'type':'email',
            'id':'Email1',
            'aria-describedby':'emailHelp',
            'placeholder':'Enter email',
            'required': 'required'
        })
    )

     password = CharField(
        max_length = 15,
        min_length = 4,
        required = True,
        label = 'Password',
        widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control mt-4'}),)
    
class AddressCreateForm(ModelForm):
    class Meta:
        model = Address
        exclude = ['user']
        widgets = {
            'name': TextInput({
                'class': 'form-control'
            }),

            'address_line_1': TextInput({
                'class': 'form-control'
            }),

            'address_line_2': TextInput({
                'class': 'form-control'
            }),

            'address_line_3': TextInput({
                'class': 'form-control'
            }),

            'city': TextInput({
                'class': 'form-control'
            }),

            'state': TextInput({
                'class': 'form-control'
            }),

            'pincode': TextInput({
                'class': 'form-control'
            }),

            'country': Select({
                'class': 'form-control'
            }),

            'phone': TextInput({
                'class': 'form-control'
            }),

            'is_default': CheckboxInput(),
        }   

class UserActivitiesForm(ModelForm):
    class Meta:
        model = UserActivity
        exclude = ['user']

    # def __init__(self, *args, **kwargs):
    #     super(UserActivity, self).__init__(*args, **kwargs)
    #     self.fields['hobbies'].queryset = Hobby.objects.all()
    #     self.fields['interests'].queryset = Interest.objects.all()

class UserQualificationsForm(ModelForm):
    class Meta:
        models = UserQualifications