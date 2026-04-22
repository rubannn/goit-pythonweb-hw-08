.PHONY: run restart clean

IMAGE_NAME = goit-fast-api
CONTAINER_NAME = app-fast-api

run:            ## Запустити контейнер (foreground)
	docker compose up

restart:        ## Перезапустити контейнер
	docker compose restart

clean:          ## Зупинити та видалити контейнер, образ і volume
	docker compose down --volumes --rmi local
	docker container prune -f
	docker image prune -a -f
	docker volume prune -f
	docker network prune -f
