from django.shortcuts import render

# Create your views here.

# Create your views here.
def register_view(request):
    return render(request,'auth/register.html')

def login_view(request):
    return render(request, 'auth/login.html')

def forgot_view(request):
    return render(request, 'auth/forgot_password.html')