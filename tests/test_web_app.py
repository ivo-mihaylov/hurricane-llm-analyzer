import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from web_app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
