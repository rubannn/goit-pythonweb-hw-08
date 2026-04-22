.PHONY: run restart makemigrations migrate migrate-docker clean

IMAGE_NAME = goit-fast-api
CONTAINER_NAME = app-fast-api

run:            ## Run containers in foreground
	docker compose up

restart:        ## Restart containers
	docker compose restart

makemigrations: ## Create a new Alembic migration
	alembic revision --autogenerate -m "auto"

migrate:        ## Apply Alembic migrations locally
	alembic upgrade head

migrate-docker: ## Apply Alembic migrations in Docker
	docker compose exec web alembic upgrade head

clean:          ## Stop and remove containers, images, volumes, networks
	docker compose down --volumes --rmi local
	docker container prune -f
	docker image prune -a -f
	docker volume prune -f
	docker network prune -f
