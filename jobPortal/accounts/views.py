from django.views.generic import TemplateView

class RegisterView(TemplateView):
    template_name = 'auth/register.html'

class LoginView(TemplateView):
    template_name = 'auth/login.html'

class ForgotPasswordView(TemplateView):
    template_name = 'auth/forgot_password.html'

