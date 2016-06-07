import json

from unittest import mock

import httpretty

from .utils import REDDIT_RESPONSE

from external_api.reddit_adapter import RedditAdapter

@httpretty.activate
def test_reddit_auth():
    httpretty.register_uri(
        httpretty.POST,
        'https://www.reddit.com/api/v1/access_token',
        body = '''{"access_token": "token",
                   "token_type": "bearer",
                   "expires_in": 3600,
                   "scope": "*"}''',
        content_type="application/json"
    )
    adapter = RedditAdapter(
        'reddit_client_id',
        'reddit_client_secret',
        'reddit_username',
        'reddit_password'
    )
    adapter.authorize()
    assert adapter.reddit_token == 'token'

@mock.patch('reddit_stars.reddit_adapter.requests.post')
@httpretty.activate
def test_reddit_search(mocked_request):
    httpretty.register_uri(
        httpretty.GET,
        "https://oauth.reddit.com/r/test/search.json?q=search&restrict_sr=on",
        body=json.dumps(REDDIT_RESPONSE),
        content_type="application/json"
    )
    adapter = RedditAdapter(
        'reddit_client_id',
        'reddit_client_secret',
        'reddit_username',
        'reddit_password'
    )
    assert adapter.search('search', 'test') == ['Post title']
