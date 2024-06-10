from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'pages/home.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class ContactView(TemplateView):
    template_name = 'pages/contact.html'



class AdminHome(TemplateView):
    template_name = 'admin-dashboard/admin-home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = [
            {
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiNqXWRkKc_N18u1Nm666PBQk3cDmKgeMm5g&s',
                'name': 'Alpha',
                'email': 'Alpha@gmail.com',
                'rating': '4.2',
                'joined': '20/02/2024',
            },
        ] * 8
        context['postings'] = [
            {
                'name': 'TCS',
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiNqXWRkKc_N18u1Nm666PBQk3cDmKgeMm5g&s',
                'email': 'TCS@gmail.com',
                'jobs': '6354',
                'open': '213',
                'joined': '5/07/2018',
            }
        ] * 8
        
        return context

class AdminCompanyDash(TemplateView):
    template_name = 'admin-dashboard/companies.html'
