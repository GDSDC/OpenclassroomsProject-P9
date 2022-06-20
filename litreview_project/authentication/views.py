from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from authentication.forms import CustomUserCreationForm, CustomAuthenticationForm


class homepage(View):
    """Redirection when no specific route is given '/'"""

    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request):
        return redirect('/feed/')


class sign_in_form(View):
    """View for home page / authentication"""

    def get(self, request):
        form = CustomAuthenticationForm(request.POST)
        return render(request, 'authentication/auth_homepage.html', {'form': form})

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

    def get(self,request):
        form = CustomUserCreationForm()
        return render(request, 'authentication/sign_up_form.html', {'form': form})

    def post(self, request):
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
            return HttpResponse('<h1>sign up form not valid</h1>')
