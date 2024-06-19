from django.views.generic import TemplateView

# Create your views here.
class UserProfileForm(TemplateView):
    template_name = 'users/complete-profile.html'
    

    
class UserHome(TemplateView):
    template_name = 'users/user-home.html'
    
class JobDetails(TemplateView):
    template_name = 'users/job-detail.html'