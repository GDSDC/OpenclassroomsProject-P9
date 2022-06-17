from django.shortcuts import render, redirect
from ticket.models import Ticket
from review.models import Review
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class posts_page(View):
    """View to see and change your own publications (ticket and/or reviews)"""

    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request):
        actual_user = request.user
        tickets = list(Ticket.objects.filter(user=actual_user))
        reviews = list(Review.objects.filter(user=actual_user))
        posts = [{'model': post.__class__.__name__, 'object': post} for post in tickets + reviews]

        return render(request, 'posts/posts.html', {'posts': posts, 'rating_range': list(range(5))})
