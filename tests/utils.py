REDDIT_RESPONSE = {
            "kind": "Listing",
            "data": {
                "facets": {},
                "modhash": "",
                "children": [
                    {
                        "kind": "t3",
                        "data": {
                            "domain": "domain",
                            "banned_by": None,
                            "media_embed": {},
                            "subreddit": "django",
                            "selftext_html": None,
                            "selftext": "",
                            "likes": None,
                            "suggested_sort": None,
                            "user_reports": [],
                            "secure_media": None,
                            "link_flair_text": None,
                            "id": "id123",
                            "from_kind": None,
                            "gilded": 0,
                            "archived": False,
                            "clicked": False,
                            "report_reasons": None,
                            "author": "author",
                            "media": None,
                            "score": 20,
                            "approved_by": None,
                            "over_18": False,
                            "hidden": False,
                            "num_comments": 4,
                            "thumbnail": "",
                            "subreddit_id": "id_sub",
                            "hide_score": False,
                            "edited": False,
                            "link_flair_css_class": None,
                            "author_flair_css_class": None,
                            "downs": 0,
                            "secure_media_embed": {},
                            "saved": False,
                            "removal_reason": None,
                            "stickied": False,
                            "from": None,
                            "is_self": False,
                            "from_id": None,
                            "permalink": "/r/django/comments/link",
                            "locked": False,
                            "name": "t3_4b7lzf",
                            "created": 1458511233,
                            "url": "http://url.com",
                            "author_flair_text": None,
                            "quarantine": False,
                            "title": "Post title",
                            "created_utc": 1458482433,
                            "distinguished": None,
                            "mod_reports": [],
                            "visited": False,
                            "num_reports": None,
                            "ups": 20
                        }
                    }
                ],
            "after": None,
            "before": None
            }
        }



class FakeRedditAdapter(object):

    def authorize(self):
        return 'oauth2-authorized-key'

    def search(self, query, subreddit=None):
        return REDDIT_RESPONSE
