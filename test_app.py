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

def test_get_dir(client):
  response = client.get('/bar')
  print(response.json)
  assert response.json == {
    "directories": [], 
    "files": [
      {
        "name": "bar1", 
        "owner": "root", 
        "permissions": "644", 
        "size": 48
      }
    ]
  }

def test_get_file(client):
  response = client.get('/foo1')
  print(response.json)
  assert response.json == {
    "content": "This is some test data in the document foo1"
  }

def test_get_error(client):
  response = client.get('/foo2')
  print(response.json)
  assert response.json == { 'error': 'path does not exist'}
  