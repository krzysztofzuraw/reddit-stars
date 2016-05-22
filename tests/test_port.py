import pytest

from tests.utils import FakeRedditAdapter

from reddit_stars.external_api_port import ExternalAPIPort


@pytest.fixture(scope='function')
def reddit_port():
    port = ExternalAPIPort(adapter=FakeRedditAdapter())
    return port


def test_reddit_search(reddit_port):
    assert list(reddit_port.search('test_search')) == ['Post title']
