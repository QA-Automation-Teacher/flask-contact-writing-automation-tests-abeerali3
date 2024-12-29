BASE_URL = "http://localhost:5000"

def setup_module(module):
    pass


def teardown_module(module):
    pass


def test_get_contacts(client):
    response = client.get("/api/contacts")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)