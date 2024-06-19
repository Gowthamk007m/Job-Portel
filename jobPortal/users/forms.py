from django import forms

from .models import *


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