from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    """Form for creating tickets"""
    class Meta:
        model = Ticket
        fields = ['title','description','image','user', 'id']

