from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from follows.models import UserFollows
from follows.forms import UserFollowForm
from django.contrib.auth.models import User


class subscriptions(View):
    """View for subscriptions page"""

    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request):
        user_follows_form = UserFollowForm()
        return render(request, 'follows/subscriptions.html', {'user_follows_form': user_follows_form})

    @method_decorator(login_required(login_url='/auth/'))
    def post(self, request):
        error_message = ""
        validation_message = ""
        actual_user = request.user
        followed_user_username = request.POST.get('followed_user', False)
        database_usernames = [user.username for user in User.objects.all()]

        if followed_user_username not in database_usernames:
            error_message = "Utilisateur inconnu !"
        elif followed_user_username == actual_user.username:
            error_message = "Veuillez renseigner un nom d'utilisateur autre que le votre."
        else:
            followed_user_id = User.objects.get(username=followed_user_username).id
            follows_form = UserFollowForm({'user': actual_user,
                                           'followed_user': followed_user_id})
            if follows_form.is_valid():
                follows_form.save()
                validation_message = f"Vous suivez désormais l'utilisateur {followed_user_username} !"
            else:
                error_message = f"Vous suivez déjà l'utilisateur {followed_user_username} !"

        user_follows_form = UserFollowForm()
        return render(request, 'follows/subscriptions.html',
                      {'user_follows_form': user_follows_form,
                       'error_message': error_message,
                       'validation_message': validation_message})
