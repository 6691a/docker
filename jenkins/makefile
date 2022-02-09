SERVICE := 'jenkins'

run:
	mkdir -p data
	export CONTAINER_NAME=$(SERVICE); docker-compose up --build -d;

stop:
	docker-compose down

log:
	docker logs -f $(SERVICE);

exec:
	docker exec -it $(SERVICE) bash;