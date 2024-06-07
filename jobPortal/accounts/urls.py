from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'), 
    path('login/', views.login_view, name='login'),
    path('forgot_password/', views.forgot_view, name='forgot_password'),
]