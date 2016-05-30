from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.shortcuts import render
from .forms import RedditSearchForm, RedditAddToFavouritesForm

class RedditSearchView(FormView):
    template_name = 'search/index.html'
    form_class = RedditSearchForm
    success_url = 'add-to-favourites'

    def form_valid(self, form):
        search_result = form.perform_search()
        return render(
            self.request,
            'search/add-to-favourites.html',
            {'search_result': search_result}
        )


class RedditAddToFavourites(FormView):
    template_name = 'search/add-to-favourites.html'
    form_class = RedditAddToFavouritesForm
    sucess_url = '/'

    def get(self, request, *args, **kwargs):
        import ipdb; ipdb.set_trace()
