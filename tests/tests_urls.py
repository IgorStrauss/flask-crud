from project import create_app


def test_route_home():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/')

        assert response.status_code == 200


def test_route_list_user_view():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/listar/')

        assert response.status_code == 200


def test_route_profile_user_view_ok():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/perfil/1/')

        assert response.status_code == 200


def test_route_profile_user_view_not_found():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/perfil/999/')

        assert response.status_code == 404


def test_route_register_user_view():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/registrar/')

        assert response.status_code == 200


def test_route_update_user_view():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/atualizar/1/')

        assert response.status_code == 200


def test_route_delete_user_view():
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/deletar/1/')

        assert response.status_code == 302
