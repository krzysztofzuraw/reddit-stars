from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from .forms import RedditAddToFavouritesFormset
from .models import RedditLink


class RedditAddToFavourites(CreateView):
    template_name = 'search/index.html'
    success_url = reverse_lazy('main_page')

    def post(self, request, *args, **kwags):
        self.object = None
        reddit_links_formset = RedditAddToFavouritesFormset(request.POST)
        if reddit_links_formset.is_valid():
            self.object = reddit_links_formset.save()
            return HttpResponseRedirect(success_url)
        else:
            return self.render_to_response(
                'search/index.html',
                self.get_context_data(
                    reddit_links_formset=reddit_links_formset
                )
            )
