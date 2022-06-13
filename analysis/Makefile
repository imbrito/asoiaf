.PHONY: build create start stop test run clean


build:
	@echo "build a docker image"
	docker build -t imbrito/asoiaf:latest .

create: build
	@echo "create a docker container"
	docker create --volume $(PWD)/data:/opt/app/data --name asoiaf -it imbrito/asoiaf

start:
	@echo "start a docker container"
	docker start asoiaf

stop:
	@echo "stop a docker container"
	docker stop asoiaf

test:
	@echo "run unit tests"
	$(MAKE) start
	docker exec -it asoiaf pytest -s -v --cov=. --cov-append --disable-warnings
	$(MAKE) stop

run:
	$(MAKE) start
	@echo "run challenge tasks"
	docker exec -it asoiaf python main.py --challenge
	$(MAKE) stop

clean: 
	@echo "clean a docker image and container"
	docker rm asoiaf
	docker rmi imbrito/asoiaf
	