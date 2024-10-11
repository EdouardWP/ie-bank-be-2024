from iebank_api import app
from iebank_api.models import Account
import pytest

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'France'})
    assert response.status_code == 200

def test_account_balance_update():
    """
    GIVEN an Account model
    WHEN the balance is updated
    THEN check if the new balance is reflected correctly
    """
    account = Account('John Doe', '€', 'France')
    account.balance = 100.0
    assert account.balance == 100.0

def test_create_account_with_invalid_name(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to with a name that contains numbers
    THEN check that the response returns an error (400 Bad Request)
    """
    # Attempt to create an account with a name containing numbers
    response = testing_client.post('/accounts', json={
        'name': 'John123',  # Invalid name (contains numbers)
        'currency': '€',
        'country': 'France'
    })

    # The response should return a 400 Bad Request status
    assert response.status_code == 400
    assert 'Invalid name' in response.get_data(as_text=True)  

def test_hello_world(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check that the response is 'Hello, World!'
    """
    response = testing_client.get('/')
    assert response.status_code == 200
    assert response.get_data(as_text=True) == 'Hello, World!'

def test_get_single_account(testing_client):
    """
    GIVEN a Flask application
    WHEN a specific account is requested (GET)
    THEN check the account details are returned correctly
    """
    # Create an account first
    create_response = testing_client.post('/accounts', json={
        'name': 'Jane Doe',
        'currency': '€',
        'country': 'Spain'
    })
    account_id = create_response.json['id']
    
    # Now retrieve that account
    response = testing_client.get(f'/accounts/{account_id}')
    assert response.status_code == 200
    assert 'Jane Doe' in response.get_data(as_text=True)


def test_update_account(testing_client):
    """
    GIVEN a Flask application
    WHEN a specific account is updated (PUT)
    THEN check that the account details are updated correctly
    """
    # Create an account
    create_response = testing_client.post('/accounts', json={
        'name': 'Jane Doe',
        'currency': '€',
        'country': 'Spain'
    })
    account_id = create_response.json['id']
    
    # Update the account's name
    update_response = testing_client.put(f'/accounts/{account_id}', json={
        'name': 'Jane Smith'
    })
    assert update_response.status_code == 200
    assert 'Jane Smith' in update_response.get_data(as_text=True)
