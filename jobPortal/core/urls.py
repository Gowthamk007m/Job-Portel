from django.urls import path
from .views import *
from  accounts.views import LoginView


app_name = 'core'  

urlpatterns = [
    path('', LoginView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]