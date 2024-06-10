from django.urls import path
from .views import *

app_name = 'core'  # Define the app name for namespacing

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    
    path('admin-home/', AdminHome.as_view(), name='admin-home'),
    path('admin-company/', AdminCompanyDash.as_view(), name='admin-company'),
    
    
]