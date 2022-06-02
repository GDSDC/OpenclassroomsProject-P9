from django.shortcuts import render

def auth_homepage(request):
    """View for home page / authentication"""
    return render(request,'authentication/auth_homepage.html')
