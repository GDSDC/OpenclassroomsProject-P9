from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def auth_homepage(request):
    """View for home page / authentication"""
    return render(request, 'authentication/auth_homepage.html')


def sign_up_form(request):
    """View for signing up with filling a form"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            return HttpResponse(f"""<h1>Nouvel utilisateur créé avec succès !!</h1>
            <p>Username : {username}</p>
            <p>Password : {raw_password}""")
        else:
            return HttpResponse('<h1>form not valid</h1>')

    else:
        form = UserCreationForm()
        return render(request, 'authentication/sign_up_form.html',{'form': form})
