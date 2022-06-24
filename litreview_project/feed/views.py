from django.shortcuts import render, redirect
from ticket.models import Ticket
from review.models import Review, RATING_CHAR, RATING_RANGE
from follows.models import UserFollows
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from itertools import chain
from django.db.models import CharField, Value


class FeedPage(View):
    """View to see and interact with publications (ticket and/or reviews)"""

    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request):
        actual_user = request.user
        subscriptions_users = [subscription.followed_user for subscription in
                               UserFollows.objects.filter(user=actual_user)]

        # // TICKETS // -------------------------------------------------------------------------------
        # tickets
        tickets = Ticket.objects.filter(user__in=[actual_user] + subscriptions_users)
        tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

        # tickets not reviewed
        tickets_not_reviewed = tickets.exclude(
            id__in=[review.ticket.id for review in Review.objects.filter(ticket__in=tickets)]).annotate(
            ticket_status=Value('not_reviewed', CharField()))

        # tickets already reviewed
        tickets_reviewed = tickets.filter(
            id__in=[review.ticket.id for review in Review.objects.filter(ticket__in=tickets)]).annotate(
            ticket_status=Value('already_reviewed', CharField()))

        # // REVIEWS // -------------------------------------------------------------------------------
        # own reviews
        own_reviews = Review.objects.filter(user=actual_user)
        own_reviews = own_reviews.annotate(content_type=Value('REVIEW', CharField()))

        # reviews in response to actual_user tickets
        reviews_actual_user_tickets = Review.objects.filter(
            ticket__in=Ticket.objects.filter(user=actual_user)).exclude(user=actual_user)
        reviews_actual_user_tickets = reviews_actual_user_tickets.annotate(content_type=Value('REVIEW', CharField()))

        # reviews from subscriptions
        subscriptions_reviews = Review.objects.filter(
            user__in=[user_follow.followed_user for user_follow in UserFollows.objects.filter(user=actual_user)])
        subscriptions_reviews = subscriptions_reviews.annotate(content_type=Value('REVIEW', CharField()))

        # // RESULT // -------------------------------------------------------------------------------
        posts = chain(tickets_not_reviewed, tickets_reviewed,
                      own_reviews, reviews_actual_user_tickets, subscriptions_reviews)

        return render(request, 'feed/feed.html',
                      context={'posts': posts,
                               'rating_range': RATING_RANGE,
                               'rating_char': RATING_CHAR})
