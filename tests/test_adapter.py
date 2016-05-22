import responses

from .utils import REDDIT_RESPONSE

from reddit_stars.reddit_adapter import RedditAdapter

@responses.activate
def test_reddit_auth():
    responses.add(
        responses.POST,
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
