from flask import render_template


def init_app(app):

    @app.route('/docs')
    def api_docs():
        endpoints = [
            {'url': '/', 'methods': 'GET', 'docstring': 'Home'},
            {'url': '/listar/', 'methods': 'GET', 'docstring': 'Listar todos os usuários cadastrados'},
            {'url': '/perfil/user_id/', 'methods': 'GET', 'docstring': 'Descrição do usuário user_id'},
            {'url': '/registrar/', 'methods': 'GET / POST', 'docstring': 'Renderiza formulário para registro de usuário'},
            {'url': '/atualizar/user_id/', 'methods': 'GET / POST', 'docstring': 'Renderiza formulário para atualizar dado(s) do usuário user_id'},
            {'url': '/deletar/user_id/', 'methods': 'GET / POST', 'docstring': 'Acessada com user_id deleta o usuário'}
        ]

        return render_template('documentation.html', endpoints=endpoints)
