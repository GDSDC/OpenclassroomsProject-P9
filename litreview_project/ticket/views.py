from django.shortcuts import render
from django.http import HttpResponse
from .forms import TicketForm
from .models import Ticket


def create_ticket(request):
    """View to create a ticket"""
    if request.method == 'POST':
        title = request.POST.get('title', False)
        description = request.POST.get('description', False)
        image = request.POST.get('image', False)
        ticket = Ticket(title=title, description=description, image=image)
        ticket.save()
        return HttpResponse(f"<h1>Votre ticket \"{title}\" a bien été enregistré !!</h1>")
    else:
        form = TicketForm()
        return render(request, 'ticket/create_ticket.html', {'form': form})
