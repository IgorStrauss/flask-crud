# bin/sh

exp-d:
	export FLASK_APP=project
	export FLASK_ENV=development

exp-t:
	export FLASK_APP=project
	export FLASK_ENV=testing

run:
	export FLASK_APP=project
	export FLASK_ENV=development
	export FLASK_DEBUG=True
	python main.py

init:
	export FLASK_APP=project
	export FLASK_ENV=development
	export FLASK_DEBUG=1
	flask db init
