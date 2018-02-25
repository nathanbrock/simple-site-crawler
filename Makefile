clean:
	docker-compose kill
	docker-compose down
	docker-compose rm

build:
	docker-compose build

start_containers: build
	docker-compose up

start_crawl:
	docker exec simplecrawler_worker_1 python -m celery_tasks.run_tasks

access_worker:
	docker exec -it simplecrawler_worker_1 bash

run_mongo:
	docker exec -it simplecrawler_database_1 mongo