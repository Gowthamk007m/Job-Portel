from django.views.generic import TemplateView

# Create your views here.
#----------------------ADMIN DASHBOARD-----------------------------

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['postings'] = [
            {
                'name': 'TCS',
                'image': 'https://seeklogo.com/images/T/tata-consultancy-services-tcs-logo-DE443D01C0-seeklogo.com.png',
                'email': 'TCS@gmail.com',
                'jobs': '6354',
                'open': '213',
                'joined': '05-07-2018',
            },
            {
                'name': 'Infosys',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Infosys_logo.svg/2560px-Infosys_logo.svg.png',
                'email': 'infosys@gmail.com',
                'jobs': '7321',
                'open': '254',
                'joined': '12-03-2019',
            },
            {
                'name': 'Wipro',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Wipro_Primary_Logo_Color.jpg/2560px-Wipro_Primary_Logo_Color.jpg',
                'email': 'wipro@gmail.com',
                'jobs': '4812',
                'open': '198',
                'joined': '15-11-2017',
            },
            {
                'name': 'HCL',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/HCLTech_logo.svg/2560px-HCLTech_logo.svg.png',
                'email': 'hcl@gmail.com',
                'jobs': '5293',
                'open': '325',
                'joined': '21-08-2020',
            },
            {
                'name': 'Tech Mahindra',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Tech_Mahindra_New_Logo.svg/2560px-Tech_Mahindra_New_Logo.svg.png',
                'email': 'techmahindra@gmail.com',
                'jobs': '3749',
                'open': '187',
                'joined': '10-01-2021',
            },
            {
                'name': 'Accenture',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/8/8d/Accenture-logo.png?20150805102421',
                'email': 'accenture@gmail.com',
                'jobs': '8256',
                'open': '443',
                'joined': '07-09-2018',
            },
            {
                'name': 'Capgemini',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Capgemini_Logo.svg/2560px-Capgemini_Logo.svg.png',
                'email': 'capgemini@gmail.com',
                'jobs': '6521',
                'open': '389',
                'joined': '30-06-2019',
            },
            {
                'name': 'Cognizant',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Cognizant%27s_logo.svg/2560px-Cognizant%27s_logo.svg.png',
                'email': 'cognizant@gmail.com',
                'jobs': '9102',
                'open': '512',
                'joined': '19-02-2022',
            },
            {
                'name': 'IBM',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/IBM_logo.svg/2560px-IBM_logo.svg.png',
                'email': 'ibm@gmail.com',
                'jobs': '7431',
                'open': '361',
                'joined': '05-04-2021',
            },
            {
                'name': 'Oracle',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Oracle_logo.svg/2560px-Oracle_logo.svg.png',
                'email': 'oracle@gmail.com',
                'jobs': '6785',
                'open': '290',
                'joined': '14-11-2020',
            }
        ]       
        
        return context

class AdminUserDash(TemplateView):
    template_name = 'admin-dashboard/users.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['users'] = [
            {   
                'profile_picture': 'https://randomuser.me/api/portraits/men/1.jpg',
                'name': 'John Doe',
                'email': 'john.doe@example.com',
                'status': 'active',
                'date_joined': '2021-05-12',
                'applications_count': 12,
                'job_postings_count': 0,
                'last_login': '2023-06-10'
            },
            {
                'profile_picture': 'https://randomuser.me/api/portraits/women/2.jpg',
                'name': 'Jane Smith',
                'email': 'jane.smith@example.com',
                'status': 'active',
                'date_joined': '2019-03-22',
                'applications_count': 0,
                'job_postings_count': 45,
                'last_login': '2023-06-09'
            },
            {
                'profile_picture': 'https://randomuser.me/api/portraits/men/3.jpg',
                'name': 'Michael Johnson',
                'email': 'michael.johnson@example.com',
                'status': 'suspended',
                'date_joined': '2020-08-10',
                'applications_count': 8,
                'job_postings_count': 0,
                'last_login': '2023-06-01'
            },
            {
                'profile_picture': 'https://randomuser.me/api/portraits/women/4.jpg',
                'name': 'Emily Davis',
                'email': 'emily.davis@example.com',
                'status': 'active',
                'date_joined': '2018-11-05',
                'applications_count': 0,
                'job_postings_count': 30,
                'last_login': '2023-06-11'
            },
            {
                'profile_picture': 'https://randomuser.me/api/portraits/men/5.jpg',
                'name': 'William Brown',
                'email': 'william.brown@example.com',
                'status': 'deactivated',
                'date_joined': '2022-01-15',
                'applications_count': 5,
                'job_postings_count': 0,
                'last_login': '2023-05-20'
            },
            {
                'profile_picture': 'https://randomuser.me/api/portraits/women/6.jpg',
                'name': 'Olivia Martinez',
                'email': 'olivia.martinez@example.com',
                'status': 'active',
                'date_joined': '2017-06-23',
                'applications_count': 0,
                'job_postings_count': 60,
                'last_login': '2023-06-08'
            },
            {
                'profile_picture': 'https://randomuser.me/api/portraits/men/7.jpg',
                'name': 'James Wilson',
                'email': 'james.wilson@example.com',
                'status': 'active',
                'date_joined': '2015-09-12',
                'applications_count': 0,
                'job_postings_count': 0,
                'last_login': '2023-06-11'
            },
            {
                'profile_picture': 'https://randomuser.me/api/portraits/women/8.jpg',
                'name': 'Sophia Taylor',
                'email': 'sophia.taylor@example.com',
                'status': 'active',
                'date_joined': '2021-02-19',
                'applications_count': 22,
                'job_postings_count': 0,
                'last_login': '2023-06-09'
            },
            {
                'profile_picture': 'https://randomuser.me/api/portraits/men/9.jpg',
                'name': 'Alexander Thomas',
                'email': 'alexander.thomas@example.com',
                'status': 'suspended',
                'date_joined': '2016-04-29',
                'applications_count': 0,
                'job_postings_count': 10,
                'last_login': '2023-05-30'
            },
            {
                'profile_picture': 'https://randomuser.me/api/portraits/women/10.jpg',
                'name': 'Isabella White',
                'email': 'isabella.white@example.com',
                'status': 'active',
                'date_joined': '2020-12-05',
                'applications_count': 14,
                'job_postings_count': 0,
                'last_login': '2023-06-07'
            }
        ] 
        
        return context

class AdminProfile(TemplateView):
    template_name = 'admin-dashboard/admin-profile.html'
    
    
class AdminAnnouncement(TemplateView):
    template_name = 'admin-dashboard/announcement.html'
    
class AddAnnouncement(TemplateView):
    template_name = 'admin-dashboard/add_announcement.html'
    
    
class AdminUserProfile(TemplateView):
    template_name = 'admin-dashboard/user-profile.html'
    

