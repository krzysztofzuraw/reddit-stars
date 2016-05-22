class ExternalAPIPort(object):

    def __init__(self, adapter):
        self.adapter = adapter

    def search(self, query, subreddit=None):
        raw_results = self.adapter.search(query, subreddit)
        for result in raw_results['data']['children']:
            yield result['data']['title']
