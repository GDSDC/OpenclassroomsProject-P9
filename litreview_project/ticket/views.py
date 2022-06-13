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
        actual_user = request.user
        if actual_user is not None and actual_user.is_active:
            ticket = Ticket(title=title, description=description, image=image, user=actual_user)
            ticket.save()
            return HttpResponse(
                f"<h1>Votre ticket \"{title}\" a bien été enregistré pour l'ulisateur \"{actual_user.username}\" !!</h1>")
        else:
            return HttpResponse(f"<h1>Utilisateur non connecté : création de ticket impossible !!</h1>")
    else:
        form = TicketForm()
        return render(request, 'ticket/create_ticket.html', {'form': form})


def posts_page(request):
    """View to see and change your own publications (ticket and/or reviews)"""
    actual_user = request.user
    if actual_user is not None and actual_user.is_active:
        tickets = Ticket.objects.filter(user=actual_user)
        return render(request, 'ticket/posts.html', {'tickets': tickets})
    else:
        return HttpResponse("<h1>ERROR</h1>")

def delete_ticket(request,id):
    """Link to delete a ticket"""
    ticket = Ticket.objects.get(id=id)
    ticket.delete()
    return posts_page(request)
