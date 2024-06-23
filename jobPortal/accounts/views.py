from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UsersignUpForm

from django.views.generic.edit import CreateView

class RegisterView(SuccessMessageMixin, CreateView):
  template_name = 'auth/register.html'
  success_url = reverse_lazy('accounts:login')
  form_class = UsersignUpForm
  success_message = "Your profile was created successfully"

# class RegisterView(TemplateView):
#     template_name = 'auth/register.html'

class LoginView(TemplateView):
    template_name = 'auth/login.html'

class ForgotPasswordView(TemplateView):
    template_name = 'auth/forgot_password.html'

