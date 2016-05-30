from django import forms
from django.conf import settings

from external_api.external_api_port import ExternalAPIPort
from external_api.reddit_adapter import RedditAdapter


class RedditSearchForm(forms.Form):
    query = forms.CharField(label='search query', max_length=100)

    def perform_search(self):
        adapter = RedditAdapter(
            settings.REDDIT_CLIENT_ID,
            settings.REDDIT_CLIENT_SECRET,
            settings.REDDIT_USERNAME,
            settings.REDDIT_PASSWORD
        )
        port = ExternalAPIPort(adapter)
        search_result = port.search(self.cleaned_data['query'])
        return search_result


class RedditAddToFavouritesForm(forms.Form):
    is_favourite = forms.BooleanField(label='favourite', initial=False)
