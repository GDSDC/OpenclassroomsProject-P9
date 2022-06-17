from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ticket.forms import TicketForm
from ticket.models import Ticket
from review.models import Review
from review.forms import ReviewForm


class create_review_ticket(View):
    """View to create a review with no ticket associated (need to create a ticket also)"""

    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request):
        review_form = ReviewForm()
        ticket_form = TicketForm()
        return render(request, 'review/create_review_ticket.html',
                      {'review_form': review_form, 'ticket_form': ticket_form})

    @method_decorator(login_required(login_url='/auth/'))
    def post(self, request):
        actual_user = request.user
        # ticket
        title = request.POST.get('title', 'test')
        description = request.POST.get('description', False)
        image = request.POST.get('image', False)
        ticket_form = TicketForm({'title': title,
                                  'description': description,
                                  'image': image,
                                  'user': actual_user},
                                 request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save()
        else:
            return HttpResponse(f"<p>ticket_form errors : {ticket_form.errors}</p>")
        # review
        headline = request.POST.get('headline', False)
        body = request.POST.get('body', False)
        rating = request.POST.get('rating', False)
        review_form = ReviewForm({'headline': headline,
                                  'body': body,
                                  'rating': rating,
                                  'user': actual_user,
                                  'ticket': ticket})
        if review_form.is_valid():
            review = review_form.save()
            return HttpResponse(f"<p>Critique '{review}' bien enregistrée !</p>")
        else:
            return HttpResponse(f"<p>review_form errors : {review_form.errors}</p>")
