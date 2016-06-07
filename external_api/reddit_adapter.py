import requests
import requests.auth

from django.conf import settings


class RedditAdapter(object):
    def __init__(
        self, reddit_client_id, reddit_client_secret,
        reddit_username, reddit_password
    ):
        self.reddit_client_id = reddit_client_id
        self.reddit_client_secret = reddit_client_secret
        self.reddit_username = reddit_username
        self.reddit_password = reddit_password
        self.reddit_token = None

    def authorize(self):
        client_auth = requests.auth.HTTPBasicAuth(
            self.reddit_client_id,
            self.reddit_client_secret
        )
        post_data = {
            "grant_type": "password",
            "username": self.reddit_username,
            "password": self.reddit_password
        }
        headers = {"User-Agent": "RedditAdapter/0.1 by Krzysztof Zuraw"}
        response = requests.post(
            "https://www.reddit.com/api/v1/access_token",
            auth=client_auth,
            data=post_data,
            headers=headers
        )
        self.reddit_token = response.json()['access_token']

    def search(self, query, subreddit=None):
        self.authorize()
        headers = {
            "Authorization": "bearer {token}".format(token=self.reddit_token),
            "User-Agent": "RedditAdapter/0.1 by Krzysztof Zuraw"
        }
        response = requests.get(
            ("https://oauth.reddit.com/r/{subreddit}/"
             "search.json?q={query}&restrict_sr={restrict}").format(
                subreddit=subreddit,
                query=query,
                restrict='on' if subreddit else 'off'
            ),
            headers=headers)
        raw_response = response.json()

        search_result = []
        for result in raw_response['data']['children']:
            search_result.append(result['data']['title'])

        return search_result


instantiated_adapter = RedditAdapter(
    settings.REDDIT_CLIENT_ID,
    settings.REDDIT_CLIENT_SECRET,
    settings.REDDIT_USERNAME,
    settings.REDDIT_PASSWORD
)
