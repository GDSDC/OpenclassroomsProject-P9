from django.shortcuts import render, redirect
from ticket.models import Ticket
from review.models import Review, RATING_CHAR, RATING_RANGE
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from itertools import chain
from django.db.models import CharField, Value


class posts_page(View):
    """View to see and change your own publications (ticket and/or reviews)"""

    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request):
        actual_user = request.user
        # tickets
        tickets = Ticket.objects.filter(user=actual_user)
        tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
        # reviews
        reviews = Review.objects.filter(user=actual_user)
        reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

        posts = chain(tickets, reviews)

        return render(request, 'posts/posts.html', context={'posts': posts,
                                                            'rating_range': RATING_RANGE,
                                                            'rating_char': RATING_CHAR})
