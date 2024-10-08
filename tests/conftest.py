import pytest
from iebank_api.models import Account
from iebank_api import db, app

@pytest.fixture(scope='module')
def testing_client():
    # Configure the app to use a test SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_ie_bank.db'
    app.config['TESTING'] = True

    with app.app_context():
        # Create the database and tables
        db.create_all()

        # Add a test account
        account = Account('Test Account', '€', 'France')
        db.session.add(account)
        db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client  # This is where the test runs

    # Teardown: Drop all tables after the test is done
    with app.app_context():
        db.drop_all()