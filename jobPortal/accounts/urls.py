from django.urls import path
from .views import *

app_name = 'accounts'  # Define the app name for namespacing

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    
    
]