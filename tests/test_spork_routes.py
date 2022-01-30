from flask import Flask
from utensils.main import spork_routes

def test_datetime():
    app = Flask(__name__)
    spork_routes(app)
    client = app.test_client()
    url = '/datetime'

    response = client.get(url)
    assert response.status_code == 200

def test_gandalf():
    app = Flask(__name__)
    spork_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.status_code == 200