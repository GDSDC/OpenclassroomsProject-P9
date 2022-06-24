from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ticket.forms import TicketForm
from ticket.models import Ticket


class CreateTicket(View):
    """View to create a ticket"""

    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request):
        form = TicketForm()
        return render(request, 'ticket/create_ticket.html', context={'form': form})

    @method_decorator(login_required(login_url='/auth/'))
    def post(self, request):
        actual_user = request.user
        title = request.POST.get('title', False)
        description = request.POST.get('description', False)
        image = request.POST.get('image', False)
        form = TicketForm({'title': title,
                           'description': description,
                           'image': image,
                           'user': actual_user},
                          request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/posts/')
        else:
            return HttpResponse(f"<p>{form.errors}</p>")


class DeleteTicket(View):
    """Link to delete a ticket"""

    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request, id):
        ticket = Ticket.objects.get(id=id)
        ticket.delete()
        return redirect('/posts/')


class EditTicket(View):
    """View to edit a ticket"""

    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request, id):
        ticket = Ticket.objects.get(id=id)
        form = TicketForm(instance=ticket)
        return render(request, 'ticket/create_ticket.html', context={'form': form, 'edit': True})

    @method_decorator(login_required(login_url='/auth/'))
    def post(self, request, id):
        ticket = Ticket.objects.get(id=id)
        actual_user = request.user
        title = request.POST.get('title', False)
        description = request.POST.get('description', False)
        image = request.POST.get('image', False)
        form = TicketForm({'title': title,
                           'description': description,
                           'image': image,
                           'user': actual_user,
                           'id': id},
                          request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('/posts/')
        else:
            return HttpResponse(f"<p>{form.errors}</p>")
