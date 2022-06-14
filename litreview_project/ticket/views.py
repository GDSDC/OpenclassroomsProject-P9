from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from ticket.forms import TicketForm
from ticket.models import Ticket
from django.contrib.auth.models import User


def create_ticket(request):
    """View to create a ticket"""
    # TODO : handle form.save() that upload image with user foreignkey issue
    # actual_user = User.objects.get(username=request.user)
    actual_user = request.user
    if actual_user is not None and actual_user.is_active:
        if request.method == 'POST':
            form = TicketForm(request.POST, request.FILES)
            if form.is_valid():
                form.user = actual_user
                form.save()
            # title = request.POST.get('title', False)
            # description = request.POST.get('description', False)
            # image = request.POST.get('image', False)
            # ticket = Ticket(title=title, description=description, image=image, user=actual_user)
            # form = TicketForm(instance=ticket)
            # form.save()
            # ticket.save()
                return redirect('/posts/')
        else:
            form = TicketForm()
            return render(request, 'ticket/create_ticket.html', {'form': form})
    else:
        return redirect('/auth/')

def show_user_infos(request):
    actual_user = request.user
    if actual_user is not None and actual_user.is_active:
        result = User.objects.get(username=actual_user).id
        return HttpResponse(f"<h1>{result}</h1>")

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
