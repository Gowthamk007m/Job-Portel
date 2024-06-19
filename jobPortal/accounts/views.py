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
                user.otp = '' 
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
    

# class PasswordResetRequestView(View):
#     def get(self, request):
#         form = EmailForm()
#         return render(request, 'password_reset_request.html', {'form': form})
    
#     def post(self, request):
#         form = EmailForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             try:
#                 user = User.objects.get(email=email)
#                 otp = get_random_string(length=6, allowed_chars='0123456789')
                
#                 # Save OTP to database
#                 OTP.objects.create(user=user, otp=otp)
                
#                 # Print OTP to console
#                 print(f"OTP for {user.email}: {otp}")
                
#                 messages.success(request, 'OTP has been generated and printed to the console.')
#                 return redirect('password_reset_confirm')
#             except User.DoesNotExist:
#                 messages.error(request, 'No user is associated with this email.')
#                 return redirect('password_reset_request')
#         return render(request, 'password_reset_request.html', {'form': form})
    

# class PasswordResetConfirmView(View):
#     def get(self, request):
#         form = OTPForm()
#         return render(request, 'password_reset_confirm.html', {'form': form})
    
#     def post(self, request):
#         form = OTPForm(request.POST)
#         if form.is_valid():
#             otp = form.cleaned_data['otp']
#             new_password = form.cleaned_data['new_password']
            
#             try:
#                 otp_obj = OTP.objects.get(otp=otp)
#                 user = otp_obj.user
#                 user.password = make_password(new_password)
#                 user.save()
                
#                 # Delete OTP after use
#                 otp_obj.delete()
                
#                 messages.success(request, 'Your password has been reset. You can now login.')
#                 return redirect('login')
#             except OTP.DoesNotExist:
#                 messages.error(request, 'Invalid OTP.')
#                 return redirect('password_reset_confirm')
#         return render(request, 'password_reset_confirm.html', {'form': form})
  