from django import forms
from review.models import Review

class ReviewForm(forms.ModelForm):
    """Form for creating reviews"""
    class Meta:
        model = Ticket
        fields = ['ticket', 'rating', 'headline', 'body', 'user']