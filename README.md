## Projeto Flask CRUD

Demonstrando neste projeto com a utilização de templates utilizando
bootstrap 4, configurando algumas variaveis em CSS, utilizando
sqlite como banco de dados

Utilizando gerenciador de bibliotecas o Poetry

Após clonar projeto, iniciar ambiente virtual.

Baixando as bibliotecas necessárias para o projeto
    pip install -r requirements.txt

Antes de dar start no projeto, necessários os comandos:
    export FLASK_APP=project
    export FLASK_ENV=development

Para inicalizar o projeto, utilizar o comando:
    python main.py

Para inicializar o banco de dados, após inicializar a aplicação:
    flask db init
    flask db migrate
    flask db upgrade


#### Rotas
 - 127.0.0.1:5000 -> Home
 - 127.0.0.1:5000/listar/ -> Renderiza lista de objetos cadastrados em ordem decrescente
 - 127.0.0.1:5000/perfil/<int:id>/ -> Renderiza os dados do objeto_id
 - 127.0.0.1:5000/registrar/ -> Rota para cadastro
 - 127.0.0.1:5000/atualizar/<int:id>/ -> Rota para atualizar um ou mais dados do objeto
 - 127.0.0.1:5000/deletar/<int:id>/ -> Deletar um objeto_id 