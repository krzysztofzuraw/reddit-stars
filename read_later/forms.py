from django import forms


class RedditAddToFavouritesForm(forms.Form):
    is_favourite = forms.BooleanField(label='favourite', initial=False)
