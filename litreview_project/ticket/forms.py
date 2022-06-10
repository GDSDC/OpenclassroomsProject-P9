from django import forms

class TicketForm(forms.Form):
    """Form for creating tickets"""
    title = forms.CharField()
    description = forms.CharField()
