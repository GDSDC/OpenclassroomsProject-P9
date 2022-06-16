from django.shortcuts import render, redirect
from ticket.models import Ticket
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class posts_page(View):
    """View to see and change your own publications (ticket and/or reviews)"""

    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request):
        actual_user = request.user
        tickets = Ticket.objects.filter(user=actual_user)
        return render(request, 'posts/posts.html', {'tickets': tickets})
