init:
	psql -c 'CREATE DATABASE wawhfd;'
	pip3 install -r requirements.txt
	npm install

build:
	pip3 install -r requirements.txt
	npm install

dev:
	webpack -d --watch

server:
	python3 manage.py runserver

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate
