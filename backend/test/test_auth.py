from app import create_app
import pytest

@pytest.fixture()
def app():
    app = create_app()
    return app

@pytest.fixture()
def client(app):
    return app.test_client()


def test_register(client):
    response = client.post('/register', data={
        'username': 'username123',
        'password': 'pass',
        'email': 'email@email.com'
    })

    assert response.status_code == 415

    response = client.post('/register', json={
        'username': 'username123',
        'password': 'pass',
        'email': 'email@email.com'
    })

    assert response.status_code == 200

def test_confirm_email(client, mocker):
    emails = []
    
    def mock_send(self, message):
        emails.append(message.__str__())

    mocker.patch('flask_mail.Mail.send', mock_send)
    
    response = client.post('/register', json={
        'username': 'username123',
        'password': 'pass',
        'email': 'email@email.com'
    })


    token = response.get_json().get('token')

    assert token is not None

    response = client.post('/confirm_email/{}'.format(token))

    assert response.status_code == 200
