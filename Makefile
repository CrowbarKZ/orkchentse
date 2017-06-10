run-db:
	docker volume create ork-pgdata
	docker run \
		-d --name ork-postgres \
		--publish=5432:5432 \
		-v ork-pgdata:/var/lib/postgresql/data \
		postgres:9.5-alpine || docker start ork-postgres
