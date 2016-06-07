from django import forms
from .models import RedditLink


class RedditAddToFavouritesForm(forms.ModelForm):
    class Meta:
        model = RedditLink
        fields = ['title', 'is_favourite']
