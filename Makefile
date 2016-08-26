dev:
	webpack -d --watch

build:
	webpack -p

server:
	python3 app.py

migrate:
	python3 manage.py db migrate

upgrade:
	python3 manage.py db upgrade
