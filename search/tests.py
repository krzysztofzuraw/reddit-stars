from unittest import mock

from django.test import TestCase, Client

from external_api.tests.utils import FakeRedditAdapter
from external_api.external_api_port import ExternalAPIPort


def mocked_reddit_adapter(func):
    def wrapper(*args, **kwargs):
        fake_adapter = FakeRedditAdapter()
        fake_port = ExternalAPIPort(fake_adapter)
        with mock.patch('search.forms.instantiated_port', autospec=True) as mocked_port:
            mocked_port.search = fake_port.search
            return func(*args, **kwargs)
    return wrapper


class RedditSearchViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    @mocked_reddit_adapter
    def test_get_search_results(self):
        response = self.client.get('/', {'query': 'test_search'})
        self.assertContains(response, 'Post title')
        self.assertIn('Post title', response.context.get('search_result'))
