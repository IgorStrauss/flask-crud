from datetime import datetime

from project import create_app


def test_register_user_view(database):
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.post('/registrar/', data={
            'first_name': 'nick',
            'last_name': 'fury',
            'username': 'nickfury',
            'email': 'nick@email.com',
            'created_at': datetime.now()
        })
        assert response.status_code == 302


def test_update_user_view(database):
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.post('/atualizar/1/', data={
            'first_name': 'nick',
            'last_name': 'fury',
            'username': 'nickfury-update',
            'email': 'nick@email.com',
            'created_at': datetime.now()
        })
        assert response.status_code == 302


def test_delete_user_view(database):
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.post('/deletar/1/')
        assert response.status_code == 302
