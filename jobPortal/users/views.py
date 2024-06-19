from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import *

# Create your views here.

def profile_complete(request):
    user = request.user
    if hasattr(user, 'profile'):
        return redirect('profile_detail', pk=user.pk)  # Redirect if profile already exists

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES)
        skill_form = SkillForm(request.POST)
        certification_form = CertificationForm(request.POST)
        education_form = EducationForm(request.POST)
        experience_form = ExperienceForm(request.POST)
        
        if (profile_form.is_valid() and skill_form.is_valid() and 
            certification_form.is_valid() and education_form.is_valid() and 
            experience_form.is_valid()):
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            skill = skill_form.save(commit=False)
            skill.user_profile = profile
            skill.save()
            
            certification = certification_form.save(commit=False)
            certification.user_profile = profile
            certification.save()
            
            education = education_form.save(commit=False)
            education.user_profile = profile
            education.save()
            
            experience = experience_form.save(commit=False)
            experience.user_profile = profile
            experience.save()
            
            return redirect('profile_success')
    else:
        profile_form = UserProfileForm()
        skill_form = SkillForm()
        certification_form = CertificationForm()
        education_form = EducationForm()
        experience_form = ExperienceForm()

    return render(request, 'users/complete-profile.html', {
        'profile_form': profile_form,
        'skill_form': skill_form,
        'certification_form': certification_form,
        'education_form': education_form,
        'experience_form': experience_form
    })
    
class UserProfileForm(TemplateView):
    template_name = 'users/complete-profile.html'
    

    
class UserHome(TemplateView):
    template_name = 'users/user-home.html'
    
class JobDetails(TemplateView):
    template_name = 'users/job-detail.html'