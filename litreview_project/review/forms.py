from django import forms
from review.models import Review


class ReviewForm(forms.ModelForm):
    """Form for creating reviews"""

    class Meta:
        model = Review
        fields = ['ticket', 'rating', 'headline', 'body', 'user']
        widgets = {
            'rating': forms.RadioSelect(choices=[(0, '- 0'), (1, '- 1'), (2, '- 2'), (3, '- 3'), (4, '- 4'), (5, '- 5')]),
        }

    # rating = forms.ChoiceField(widget=forms.RadioSelect(choices=rating_choices), label="")
