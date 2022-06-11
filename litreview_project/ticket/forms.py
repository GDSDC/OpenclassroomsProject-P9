from django import forms

class TicketForm(forms.Form):
    """Form for creating tickets"""
    title = forms.CharField(max_length=128)
    description = forms.CharField(max_length=2048)
    image = forms.ImageField()
    time_created = forms.DateTimeField()