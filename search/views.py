from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.shortcuts import render
from .forms import RedditSearchForm
from read_later.forms import RedditAddToFavouritesFormset


class RedditSearchView(FormView):
    template_name = 'search/index.html'
    form_class = RedditSearchForm
    success_url = 'add-to-favourites'
    search_result = None

    def get(self, request, *args, **kwargs):
        form = self.form_class(self.request.GET or None)
        if form.is_valid():
            self.search_result = form.perform_search()
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(RedditSearchView, self).get_context_data(**kwargs)
        if self.search_result:
            reddit_links_formset = RedditAddToFavouritesFormset(
                initial=[{'title': title} for title in self.search_result[:5]]
            )
            context.update({
                'search_result': self.search_result,
                'sucess': True,
                'reddit_links_formset':reddit_links_formset,
                }
            )
        return context
