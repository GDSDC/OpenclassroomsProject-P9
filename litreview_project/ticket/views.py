from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from ticket.forms import TicketForm
from ticket.models import Ticket


def create_ticket(request):
    """View to create a ticket"""
    actual_user = request.user
    if actual_user is not None and actual_user.is_active:
        if request.method == 'POST':
            title = request.POST.get('title', False)
            description = request.POST.get('description', False)
            image = request.POST.get('image', False)
            ticket = Ticket(title=title, description=description, image=image, user=actual_user)
            ticket.save()
            return redirect('/posts/')
        else:
            form = TicketForm()
            return render(request, 'ticket/create_ticket.html', {'form': form})
    else:
        return redirect('/authentication/')



def delete_ticket(request, id):
    """Link to delete a ticket"""
    ticket = Ticket.objects.get(id=id)
    ticket.delete()
    return redirect('/posts/')


def edit_ticket(request, id):
    """View to edit a ticket"""
    if request.method == 'POST':
        title = request.POST.get('title', False)
        description = request.POST.get('description', False)
        # image = request.POST.get('image', False)
        ticket = Ticket.objects.get(id=id)
        ticket.title = title
        ticket.description = description
        # title.image=image
        ticket.save()
        return redirect('/posts/')
    else:
        ticket = Ticket.objects.get(id=id)
        form = TicketForm(instance=ticket)
        return render(request, 'ticket/create_ticket.html', {'form': form})
