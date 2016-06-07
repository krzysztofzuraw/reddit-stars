from django import forms

from external_api.external_api_port import instantiated_port


class RedditSearchForm(forms.Form):
    query = forms.CharField(label='search query', max_length=100)

    def perform_search(self):
        search_result = instantiated_port.search(self.cleaned_data['query'])
        return search_result
