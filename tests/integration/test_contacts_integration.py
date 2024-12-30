import pytest
from app import app
from models import db, Contacts
from faker import Factory
from migrations import generate_fake_contacts


def setup_module(module):
    with app.app_context():
        # Clear the database before running tests
        db.drop_all()
        db.create_all()
        generate_fake_contacts(100)


def teardown_module(module):
    with app.app_context():
        # Drop all tables after running tests
        db.session.remove()
        db.drop_all()


def test_get_contacts(client, BASE_URL, contacts_num):
    response = client.get(BASE_URL + "/api/contacts")
    assert response.status_code == 200
    print(response.get_json())
    assert isinstance(response.get_json(), list)
    assert len(response.get_json()) == contacts_num
    

def test_create_contact(client, BASE_URL):
    new_contact = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "123-456-7890"
    }
    response = client.post(BASE_URL + "/api/contacts", json=new_contact)
    assert response.status_code == 201
    created_contact = response.get_json()
    assert created_contact["name"] == new_contact["name"]
    assert created_contact["email"] == new_contact["email"]
    assert created_contact["phone"] == new_contact["phone"]


def test_update_contact(client, BASE_URL):
    updated_contact = {
        "name": "Jane",
        "surname": "Doe",
        "email": "jane.doe@example.com",
        "phone": "098-765-4321"
    }
    response = client.put(BASE_URL + "/api/contacts/1", json=updated_contact)
    assert response.status_code == 200
    updated_contact_response = response.get_json()
    assert updated_contact_response["name"] == updated_contact["name"]
    assert updated_contact_response["email"] == updated_contact["email"]
    assert updated_contact_response["phone"] == updated_contact["phone"]


def test_delete_contact(client, BASE_URL):
    response = client.delete(BASE_URL + "/api/contacts/1")
    assert response.status_code == 204




# def test_get_contacts(client):
#     response = client.get("/api/contacts")
#     assert response.status_code == 200
#     assert isinstance(response.get_json(), list)
    
# def test_get_contacts_name(client):
#     response = client.get("/api/contacts")
#     assert response.status_code == 200
#     data = response.get_json()
#     for contact in data:
#         assert 'name' in contact
      
# def test_get_contacts_surname(client):
#     response = client.get("/api/contacts")
#     data = response.get_json()
#     assert isinstance(data, list)
#     for contact in data:
#         assert 'surname' in contact
        
# def test_get_non_existing_endpoint(client):
#     response = client.get("/api/non_existing_endpoint")
#     assert response.status_code == 404


# import time

# def test_get_contacts_response_time(client):
#     start_time = time.time()
#     response = client.get("/api/contacts")
#     end_time = time.time()
#     assert response.status_code == 200
#     assert end_time - start_time < 0.5  
    
# def test_create_contact(client):
#     new_contact = {
#         "name": "John Doe",
#         "email": "john.doe@example.com",
#         "phone": "123-456-7890"
#     }
#     response = client.post("/api/contacts", json=new_contact)
#     assert response.status_code == 201
#     data = response.get_json()
#     assert data["name"] == new_contact["name"]
#     assert data["email"] == new_contact["email"]
#     assert data["phone"] == new_contact["phone"]
