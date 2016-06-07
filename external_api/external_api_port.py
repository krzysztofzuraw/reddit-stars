from .reddit_adapter import instantiated_adapter

class ExternalAPIPort(object):

    def __init__(self, adapter):
        self.adapter = adapter

    def search(self, query, *args, **kwargs):
        return self.adapter.search(query, *args, **kwargs)

instantiated_port = ExternalAPIPort(instantiated_adapter)
