from django.views.generic.edit import FormView
from .forms import RedditAddToFavouritesForm


class RedditAddToFavourites(FormView):
    template_name = 'search/index.html'
    form_class = RedditAddToFavouritesForm
    sucess_url = '/'
