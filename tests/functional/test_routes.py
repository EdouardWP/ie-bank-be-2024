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

def test_delete_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts/<id>' page is deleted (DELETE)
    THEN check the response is valid and the account is deleted
    """
    # First, create an account
    response = testing_client.post('/accounts', json={
        'name': 'Jane Doe',
        'currency': '€',
        'country': 'Germany'
    })
    assert response.status_code == 200
   


