SERVICE := 'jenkins'
DOCKER_GID := 43794
run:
	mkdir -p data
	sudo groupmod -g ${DOCKER_GID} docker
	export DOCKER_GID=$(DOCKER_GID); export CONTAINER_NAME=$(SERVICE); docker-compose up --build -d;

stop:
	docker-compose down

log:
	docker logs -f $(SERVICE);

exec:
	docker exec -it $(SERVICE) bash;