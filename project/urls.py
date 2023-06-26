from flask import abort, flash, redirect, render_template, request, url_for
from sqlalchemy import text

from project.models import User, db


def init_app(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/listar/', methods=['GET'], endpoint='listar')
    def list_user_view():
        users = User.query.order_by(text('-id'))
        return render_template('listar-usuarios.html', users=users)

    @app.route('/perfil/<int:id>/', methods=['GET'], endpoint='user_id')
    def profile_user_view(id):
        user =  User.query.get(id)
        if user:
            return render_template('perfil-usuario.html', user=user)
        abort(404)

    @app.route('/registrar/', methods=['GET', 'POST'], endpoint='registrar')
    def register_user_view():
        if request.method == 'POST':
            user = User()
            user.first_name = request.form['first_name']
            user.last_name = request.form['last_name']
            user.username = request.form['username']
            user.email = request.form['email']
            db.session.add(user)
            db.session.commit()
            flash('Cadastro realizado com sucesso', category='success')
            return redirect(url_for('listar'))
        return render_template('cadastrar-usuario.html')

    @app.route('/atualizar/<int:id>/', methods=['GET', 'POST'], endpoint='update_user_id')
    def update_user(id):
        user = User.query.get(id)

        if not user:
            flash('Usuário não encontrado', category='error')
            return redirect(url_for('listar'))

        if request.method == 'POST':
            user.first_name = request.form['first_name']
            user.last_name = request.form['last_name']
            user.username = request.form['username']
            user.email = request.form['email']

            db.session.commit()

            flash('Usuário atualizado com sucesso', category='success')
            return redirect(url_for('listar'))

        return render_template('atualizar-usuario.html', user=user)

    @app.route('/deletar/<int:id>/', methods=['GET', 'POST'], endpoint='deletar_user_id')
    def delete_user_view(id):
        user = User.query.get(id)
        if user is not None:
            db.session.delete(user)
            db.session.commit()
            flash('Deletado com sucesso', category='success')
        return redirect(url_for('listar'))
