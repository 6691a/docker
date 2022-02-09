DOCKER_GROUP_ID := $(shell getent group docker | awk -F: '{printf "%d",$$3}')

SERVICE := 'jenkins'

run:
	export DOCKER_GROUP_ID=$(DOCKER_GROUP_ID)
	docker-compose up --build -d

log:
	docker logs -f $(SERVICE)

exec:
	docker exec -it $(SERVICE) sh -c "((clear && bash) || (clear && sh))"