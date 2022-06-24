from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ticket.forms import TicketForm
from ticket.models import Ticket
from review.models import Review
from review.forms import ReviewForm


class CreateReviewTicket(View):
    """View to create a review with no ticket associated (need to create a ticket also)"""

    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request):
        review_form = ReviewForm()
        ticket_form = TicketForm()
        return render(request, 'review/create_review_ticket.html', context={'review_form': review_form,
                                                                            'ticket_form': ticket_form})

    @method_decorator(login_required(login_url='/auth/'))
    def post(self, request):
        actual_user = request.user
        # ticket
        title = request.POST.get('title', False)
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
            review_form.save()
            return redirect('/posts/')
        else:
            return HttpResponse(f"<p>review_form errors : {review_form.errors}</p>")


class CreateReviewFromTicket(View):
    """View to create a review in response to a ticket (no need to create a ticket)"""

    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request, ticket_id):
        review_form = ReviewForm()
        ticket = Ticket.objects.get(id=ticket_id)
        return render(request, 'review/create_review_from_ticket.html', context={'review_form': review_form,
                                                                                 'ticket': ticket})

    @method_decorator(login_required(login_url='/auth/'))
    def post(self, request, ticket_id):
        # ticket
        ticket = Ticket.objects.get(id=ticket_id)
        # review
        actual_user = request.user
        headline = request.POST.get('headline', False)
        body = request.POST.get('body', False)
        rating = request.POST.get('rating', False)
        review_form = ReviewForm({'headline': headline,
                                  'body': body,
                                  'rating': rating,
                                  'user': actual_user,
                                  'ticket': ticket})
        if review_form.is_valid():
            review_form.save()
            return redirect('/posts/')
        else:
            return HttpResponse(f"<p>review_form errors : {review_form.errors}</p>")


class DeleteReview(View):
    """Link to delete a review"""

    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request, review_id):
        review = Review.objects.get(id=review_id)
        review.delete()
        return redirect('/posts/')


class EditReview(View):
    """View to edit a review"""

    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request, review_id):
        review = Review.objects.get(id=review_id)
        review_form = ReviewForm(instance=review)
        ticket = Ticket.objects.get(id=review.ticket.id)
        return render(request, 'review/create_review_from_ticket.html', context={'review_form': review_form,
                                                                                 'ticket': ticket,
                                                                                 'edit': True})

    @method_decorator(login_required(login_url='/auth/'))
    def post(self, request, review_id):
        review = Review.objects.get(id=review_id)
        ticket = Ticket.objects.get(id=review.ticket.id)
        actual_user = request.user
        headline = request.POST.get('headline', False)
        body = request.POST.get('body', False)
        rating = request.POST.get('rating', False)
        review_form = ReviewForm({'headline': headline,
                                  'body': body,
                                  'rating': rating,
                                  'user': actual_user,
                                  'ticket': ticket}, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('/posts/')
        else:
            return HttpResponse(f"<p>{form.errors}</p>")
