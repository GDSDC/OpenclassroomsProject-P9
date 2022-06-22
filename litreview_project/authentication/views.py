from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from authentication.forms import CustomUserCreationForm, CustomAuthenticationForm
from urllib.parse import urlencode

_MESSAGES = {
    'not_same_password': "Vous avez entré deux mots de passe différents.",
    'username_already_used': "Le nom d'utilisateur '{username}' est déjà utilisé."
}


class homepage(View):
    """Redirection when no specific route is given '/'"""

    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request):
        return redirect('/feed/')


class sign_in_form(View):
    """View for home page / authentication"""

    def get(self, request):
        form = CustomAuthenticationForm(request.POST)
        return render(request, 'authentication/auth_homepage.html', context={'form': form})

    def post(self, request):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/feed/')
        else:
            return HttpResponse('<h1>sign in form not valid</h1>')


class sign_up_form(View):
    """View for signing up with filling a form"""

    def get(self, request):
        form = CustomUserCreationForm()

        error_message = request.GET.get('error_message') if request.GET.get('error_message') != 'None' else None
        username = request.GET.get('username') if request.GET.get('username') != 'None' else None

        if error_message is not None:
            error_message = _MESSAGES[error_message].format(username=username)
        else:
            error_message = None

        return render(request, 'authentication/sign_up_form.html', context={'form': form,
                                                                            'error_message': error_message})

    def post(self, request):
        username = request.POST.get('username', False)

        if User.objects.filter(username=username).exists():
            error_message = 'username_already_used'
            query = {'error_message': error_message,
                     'username': username}
            query_string = urlencode(query)

            return redirect(f'/auth/sign_up/?{query_string}')

        else:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                # REAL LIFE ACTION BELLOW to uncomment
                # return redirect('/auth/')

                # FOR DEBUGGING ONLY
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                if user is not None and user.is_active:
                    login(request, user)
                    return redirect('/feed/')
                # TODO : uncomment REAL LIFE ACTION and comment FOR DEBUGGING ONLY

            else:
                error_message = 'not_same_password'
                query = {'error_message': error_message}
                query_string = urlencode(query)

                return redirect(f'/auth/sign_up/?{query_string}')
