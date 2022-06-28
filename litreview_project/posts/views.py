from django.shortcuts import render, redirect
from ticket.models import Ticket
from review.models import Review, RATING_CHAR_ON, RATING_CHAR_OFF, RATING_RANGE
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from itertools import chain
from django.db.models import CharField, Value


class PostsPage(View):
    """View to see and change your own publications (ticket and/or reviews)"""

    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request):
        actual_user = request.user

        # // TICKETS // -------------------------------------------------------------------------------
        # own tickets
        own_tickets = Ticket.objects.filter(user=actual_user)
        own_tickets = own_tickets.annotate(content_type=Value('TICKET', CharField()))

        # own tickets not reviewed
        own_tickets_not_reviewed = own_tickets.exclude(
            id__in=[review.ticket.id for review in Review.objects.filter(ticket__in=own_tickets)]).annotate(
            ticket_status=Value('not_reviewed', CharField()))

        # own tickets already reviewed
        own_tickets_reviewed = own_tickets.filter(
            id__in=[review.ticket.id for review in Review.objects.filter(ticket__in=own_tickets)]).annotate(
            ticket_status=Value('already_reviewed', CharField()))

        # // REVIEWS // -------------------------------------------------------------------------------
        # own reviews
        own_reviews = Review.objects.filter(user=actual_user)
        own_reviews = own_reviews.annotate(content_type=Value('REVIEW', CharField()))

        # result
        posts = chain(own_tickets_not_reviewed, own_tickets_reviewed, own_reviews)

        return render(request, 'posts/posts.html', context={'posts': posts,
                                                            'rating_range': RATING_RANGE,
                                                            'rating_char_on': RATING_CHAR_ON,
                                                            'rating_char_off': RATING_CHAR_OFF})
