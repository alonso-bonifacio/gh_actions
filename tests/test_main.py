import pytest
import random
import string

import app as main

@pytest.fixture()
def app():
    yield main.app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_request_default(client):
    response = client.get("/")
    assert into_div("World") in response.data

def test_request_github(client):
    response = client.get("/GitHub")
    assert into_div("GitHub") in response.data

def test_request_amigo(client):
    response = client.get("/amigo")
    assert into_div("amigo") in response.data

def test_request_random(client):
    name = random_string()
    response = client.get("/{}".format(name))
    assert into_div(name) in response.data

def random_string():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))

def into_div(text):
    return "<div class=\"intro\">Hello {}!</div>".format(text).encode()
