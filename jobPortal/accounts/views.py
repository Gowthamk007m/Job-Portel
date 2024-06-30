from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login

from .models import *
from .forms import CustomUserCreationForm, LoginForm,UserDetailsForm
from django.contrib import messages
from django.views.generic import CreateView,UpdateView
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



class HobbyCreateView(LoginRequiredMixin, CreateView):
    form_class = UserDetailsForm
    template_name = 'users/user_details.html'
    success_url = reverse_lazy('users:jobs')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
# class UserHobbyUpdateView(UpdateView):
#     model = UserHobby
#     form_class = UserHobbyForm
#     template_name = 'user_hobby_form.html'
#     context_object_name = 'user_hobby'

#     def get_object(self):
#         user_id = self.kwargs.get('user_id')
#         user_hobby, created = UserHobby.objects.get_or_create(user_id=user_id)
#         return user_hobby

#     def get_success_url(self):
#         return reverse_lazy('some_view_name')