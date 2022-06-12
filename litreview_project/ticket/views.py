from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .forms import TicketForm
from .models import Ticket


def create_ticket(request):
    """View to create a ticket"""
    if request.method == 'POST':
        title = request.POST.get('title', False)
        description = request.POST.get('description', False)
        image = request.POST.get('image', False)
        user = request.user
        if user is not None and user.is_active:
            ticket = Ticket(title=title, description=description, image=image, user=user)
            ticket.save()
            return HttpResponse(
                f"<h1>Votre ticket \"{title}\" a bien été enregistré pour l'ulisateur \"{user.username}\" !!</h1>")
        else:
            return HttpResponse(f"<h1>Utilisateur non connecté : création de ticket impossible !!</h1>")
    else:
        form = TicketForm()
        return render(request, 'ticket/create_ticket.html', {'form': form})
