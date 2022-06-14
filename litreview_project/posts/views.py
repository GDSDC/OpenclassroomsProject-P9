from django.shortcuts import render, redirect
from ticket.models import Ticket
from django.http import HttpResponse


def posts_page(request):
    """View to see and change your own publications (ticket and/or reviews)"""
    actual_user = request.user
    if actual_user is not None and actual_user.is_active:
        tickets = Ticket.objects.filter(user=actual_user)
        return render(request, 'posts/posts.html', {'tickets': tickets})
    else:
        return redirect('/authentication/')