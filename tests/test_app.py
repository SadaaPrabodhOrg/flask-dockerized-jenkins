import pytest
from src.index import *


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_root(client):
    """Test the default route."""

    res = client.get('/')
    assert b'Hello world! Hi ferozekhan' in res.data


def test_status(client):
    """Test the status route."""

    res = client.get('/status')
    assert b'{"status":"UP"}' in res.data
