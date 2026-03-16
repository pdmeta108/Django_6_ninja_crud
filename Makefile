DEV_COMPOSE_FILE := docker-compose.yml

build:
	docker build -t django-app:latest -f Dockerfile .

lint:
	ruff format

dev-stack-up:
	docker compose -f $(DEV_COMPOSE_FILE) up --build