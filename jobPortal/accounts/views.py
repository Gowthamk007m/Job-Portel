from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth import login
from django.shortcuts import render
from .forms import *
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth import logout

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'auth/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until OTP is verified
            user.save()
            user.generate_otp()
            print(f"OTP for {user.email}: {user.otp}")  # Output OTP to the console
            request.session['user_id'] = user.id
            return redirect('accounts:otp_verify')
        return render(request, 'auth/register.html', {'form': form})

class OTPVerifyView(View):
    def get(self, request):
        form = OTPForm()
        return render(request, 'auth/otp_verify.html', {'form': form})

    def post(self, request):
        form = OTPForm(request.POST)
        user_id = request.session.get('user_id')
        user = CustomUser.objects.get(id=user_id)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            if user.otp == otp:
                user.is_active = True
                user.otp = ''  # Clear OTP field
                user.save()
                return redirect(reverse_lazy('users:complete-profile'))
            else:
                form.add_error('otp', 'Invalid OTP')
        return render(request, 'auth/otp_verify.html', {'form': form})

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




class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:login')