from django.urls import path
from .views import *

app_name = 'accounts' 

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('otp-verify/', OTPVerifyView.as_view(), name='otp_verify'),
    path('logout/', LogoutView.as_view(), name='logout'),
]