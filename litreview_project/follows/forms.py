from django import forms
from follows.models import UserFollows


class UserFollowForm(forms.ModelForm):
    """Form to follow other user"""

    class Meta:
        model = UserFollows
        fields = ['user', 'followed_user']
        widgets = {
            'followed_user': forms.TextInput(attrs={'placeholder': 'Nom d\'utilisateur'})
        }
