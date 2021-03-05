from app import create_app
import pytest

@pytest.fixture
def app():
  return create_app()

@pytest.fixture
def client(app):
  return app.test_client()

def test_get_root(client):
  response = client.get('/')
  print(response.json)
  assert response.json == {
    "directories": [
      "bar"
    ], 
    "files": [
      {
        "name": "foo1", 
        "owner": "root", 
        "permissions": "644", 
        "size": 43
      }
    ]
  }
  