from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth import login
from django.shortcuts import render
from .forms import *
from django.contrib.auth.views import LoginView as BaseLoginView

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'auth/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('accounts:login'))
        return render(request, 'auth/register.html', {'form': form})
    

class LoginView(View):
    def get(self, request):
        form = CustomAuthenticationForm()
        return render(request, 'auth/login.html', {'form': form})

    def post(self, request):
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('users:jobs') 
        return render(request, 'auth/login.html', {'form': form})

class ForgotPasswordView(TemplateView):
    template_name = 'auth/forgot_password.html'




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

    return render(request, 'profile_complete.html', {
        'profile_form': profile_form,
        'skill_form': skill_form,
        'certification_form': certification_form,
        'education_form': education_form,
        'experience_form': experience_form
    })