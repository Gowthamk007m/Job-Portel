from django.urls import path
from .views import *

app_name = 'accounts' 

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user-activities/create/', UserActivitiesCreateView.as_view(), name='ActivitiesCreateView'),    

]