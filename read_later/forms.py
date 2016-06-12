from django import forms
from .models import RedditLink

RedditAddToFavouritesFormset = forms.modelformset_factory(
    RedditLink,
    fields=('title', 'is_favourite'),
    extra=5
)
