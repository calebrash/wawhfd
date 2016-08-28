build:
	pip3 install -r requirements.txt
	npm install

dev:
	webpack -d --watch

server:
	python3 app.py

migrate:
	python3 manage.py db migrate

upgrade:
	python3 manage.py db upgrade
