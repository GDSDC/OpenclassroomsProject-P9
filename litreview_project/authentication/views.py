from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from authentication.forms import CustomUserCreationForm, CustomAuthenticationForm

def homepage(request):
    """Redirection when no specific route is given '/'"""
    actual_user = request.user = request.user
    if actual_user is not None and actual_user.is_active:
        return redirect('/posts/')
    else:
        return redirect('/authentication/')

def sign_in_form(request):
    """View for home page / authentication"""
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/create_ticket/')
        else:
            return HttpResponse('<h1>sign in form not valid</h1>')

    else:
        form = CustomAuthenticationForm(request.POST)
        return render(request, 'authentication/auth_homepage.html', {'form': form})


def sign_up_form(request):
    """View for signing up with filling a form"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # REAL LIFE ACTION BELLOW to uncomment
            # return redirect('/authentication/')

            # FOR DEBUGGING ONLY
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('/create_ticket/')
            # TODO : uncomment REAL LIFE ACTION and comment FOR DEBUGGING ONLY

        else:
            return HttpResponse('<h1>sign up form not valid</h1>')

    else:
        form = CustomUserCreationForm()
        return render(request, 'authentication/sign_up_form.html', {'form': form})
