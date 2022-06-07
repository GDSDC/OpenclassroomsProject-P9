from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, CustomAuthenticationForm


def auth_homepage(request):
    """View for home page / authentication"""
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponse(f"""<h1>Nouvel connexion effectuée avec succès !!</h1>
            <p>Username : {username}</p>
            <p>Password : {password}</p>""")
        else:
            return HttpResponse('<h1>form not valid</h1>')

    else:
        form = CustomAuthenticationForm(request.POST)
        return render(request, 'authentication/auth_homepage.html', {'form': form})


def sign_up_form(request):
    """View for signing up with filling a form"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            return HttpResponse(f"""<h1>Nouvel utilisateur créé avec succès !!</h1>
            <p>Username : {username}</p>
            <p>Password : {raw_password}</p>""")
        else:
            return HttpResponse('<h1>form not valid</h1>')

    else:
        form = CustomUserCreationForm()
        return render(request, 'authentication/sign_up_form.html', {'form': form})
