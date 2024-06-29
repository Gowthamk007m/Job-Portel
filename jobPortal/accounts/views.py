from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, LoginForm
from django.contrib import messages
from django.views.generic import CreateView
from django.views import View
from django.contrib.auth import logout 


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'auth/register.html'
    success_url = reverse_lazy('accounts:login')
    form_class = CustomUserCreationForm


class LoginView(View):
    form_class = LoginForm
    template_name = 'auth/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('users:jobs')
            else:
                form.add_error(None, "Invalid email or password.")
                return render(request, self.template_name, {'form': form})


class ForgotPasswordView(TemplateView):
    template_name = 'auth/forgot_password.html'


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:login')
