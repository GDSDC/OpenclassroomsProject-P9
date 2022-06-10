from django.shortcuts import render
from .forms import TicketForm


def create_ticket(request):
    """View to create a ticket"""
    form = TicketForm()
    return render(request, 'ticket/create_ticket.html', {'form': form})
