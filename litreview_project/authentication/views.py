from django.shortcuts import render

def auth_homepage(request):
    """View for home page / authentication"""
    return render(request,'authentication/auth_homepage.html')

def sign_up_form(request):
    """View for signing up with filling a form"""
    return render(request,'authentication/sign_up_form.html')
