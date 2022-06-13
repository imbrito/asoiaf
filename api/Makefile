.PHONY: build create start stop test run clean


build:
	@echo "build a docker compose services"
	docker-compose build

start: build
	@echo "start a docker container"
	docker-compose up -d

stop:
	@echo "stop a docker container"
	docker-compose stop

test:
	@echo "run unit tests"
	$(MAKE) start
	docker exec -it flask-api pytest -s -v --cov=. --cov-append --disable-warnings
	$(MAKE) stop

clean: 
	@echo "clean a docker image and container"
	docker-compose down
	