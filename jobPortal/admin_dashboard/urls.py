from django.urls import path
from .views import *

app_name = 'admin_dashboard' 

urlpatterns = [
    path('', AdminHome.as_view(), name='admin-home'),
    path('admin-company/', AdminCompanyDash.as_view(), name='admin-company'),
    path('admin-users/', AdminUserDash.as_view(), name='admin-users'),
    path('admin-profile/', AdminProfile.as_view(), name='admin-profile'),
    path('admin-announcement/', AdminAnnouncement.as_view(), name='admin-announcement'),
    path('admin-announcement-add/', AddAnnouncement.as_view(), name='admin-announcement-add'),
    path('admin-user-profile/', AdminUserProfile.as_view(), name='admin-user-profile'),  
]