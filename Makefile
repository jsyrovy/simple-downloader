PYTHON=venv/bin/python3

.DEFAULT:
	help

help:
	@echo "make help"
	@echo "  show help"
	@echo "make init"
	@echo "  create venv and install requirements"
	@echo "make run"
	@echo "  run simple-downloader"
	@echo "make docker-run"
	@echo "  run container"
	@echo "make docker-start"
	@echo "  start container"
	@echo "make docker-remove-container"
	@echo "  remove container"
	@echo "make docker-remove-image"
	@echo "  remove image"
	@echo "make docker-remove"
	@echo "  remove container and image"

init:
	python3 -m venv venv
	${PYTHON} -m pip install -r requirements.txt

run:
	${PYTHON} autoapp.py

docker-build:
	docker build . -t jsyrovy/simple-downloader

docker-run:
	docker run -v $(shell pwd)/downloads:/app/downloads -p 80:80 --name simple-downloader -it jsyrovy/simple-downloader

docker-start:
	docker start -ai simple-downloader

docker-remove-container:
	docker rm simple-downloader

docker-remove-image:
	docker rmi jsyrovy/simple-downloader

docker-remove: docker-remove-container docker-remove-image
