from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from urllib.parse import urlencode
from follows.models import UserFollows
from follows.forms import UserFollowForm

_MESSAGES = {
    'unknown_user': "Utilisateur inconnu !",
    'do_not_follow_yourself': "Veuillez renseigner un nom d'utilisateur autre que le votre.",
    'subscription_succes': "Vous suivez désormais l'utilisateur {username} !",
    'already_following': "Vous suivez déjà l'utilisateur {username} !",
    'stopped_subscription': "Vous ne suivez désormais plus l'utilisateur {username}"

}


class Subscriptions(View):
    """View for subscriptions page"""

    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request):
        user_follows_form = UserFollowForm()
        actual_user = User.objects.get(username=request.user.username)
        user_subscriptions = list(UserFollows.objects.filter(user=actual_user))
        subscribers = [user_follow.user for user_follow in UserFollows.objects.filter(followed_user=actual_user)]

        error_message = request.GET.get('error_message') if request.GET.get('error_message') != 'None' else None
        validation_message = request.GET.get('validation_message') if request.GET.get(
            'validation_message') != 'None' else None
        followed_user = request.GET.get('followed_user') if request.GET.get('followed_user') != 'None' else None
        if error_message is not None:
            error_message = _MESSAGES[error_message].format(username=followed_user)
        else:
            error_message = None
        if validation_message is not None:
            validation_message = _MESSAGES[validation_message].format(username=followed_user)
        else:
            validation_message = None

        return render(request, 'follows/subscriptions.html', context={'user_follows_form': user_follows_form,
                                                                      'subscriptions': user_subscriptions,
                                                                      'subscribers': subscribers,
                                                                      'error_message': error_message,
                                                                      'validation_message': validation_message})

    @method_decorator(login_required(login_url='/auth/'))
    def post(self, request):
        error_message = None
        validation_message = None
        actual_user = request.user
        followed_user_username = request.POST.get('followed_user', False)

        if not User.objects.filter(username=followed_user_username).exists():
            error_message = 'unknown_user'
        elif followed_user_username == actual_user.username:
            error_message = 'do_not_follow_yourself'
        else:
            followed_user_id = User.objects.get(username=followed_user_username).id
            follows_form = UserFollowForm({'user': actual_user,
                                           'followed_user': followed_user_id})
            if follows_form.is_valid():
                follows_form.save()
                validation_message = 'subscription_succes'
            else:
                error_message = 'already_following'

        query = {'error_message': error_message,
                 'validation_message': validation_message,
                 'followed_user': followed_user_username}
        query_string = urlencode(query)

        return redirect(f'/subscriptions/?{query_string}')


class DeleteSubscription(View):
    """Link to delete subscription"""

    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request, followed_user_id):
        actual_user = request.user
        followed_user = User.objects.get(id=followed_user_id)
        subscription_to_delete = UserFollows.objects.get(user=actual_user,
                                                         followed_user=followed_user)
        subscription_to_delete.delete()
        validation_message = 'stopped_subscription'

        query = {'validation_message': validation_message,
                 'followed_user': followed_user.username}
        query_string = urlencode(query)

        return redirect(f'/subscriptions/?{query_string}')
