
kroki:
	docker-compose up -d

mkdocs:
	docker build -t doc-builder .
	docker run -v ${PWD}:/usr/src/app doc-builder build