import pytest

from .utils import FakeRedditAdapter

from external_api.external_api_port import ExternalAPIPort


@pytest.fixture(scope='function')
def reddit_port():
    port = ExternalAPIPort(adapter=FakeRedditAdapter())
    return port


def test_reddit_search(reddit_port):
    assert reddit_port.search('test_search') == ['Post title']
