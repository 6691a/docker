DOCKER_GID := $(shell getent group docker)

SERVICE := 'jenkins'

run:
	export DOCKER_GID=$(DOCKER_GID)
	export

stop:
	docker-compose down

log:
	docker logs -f $(SERVICE)

exec:
	docker exec -it $(SERVICE) sh -c "((clear && bash) || (clear && sh))"