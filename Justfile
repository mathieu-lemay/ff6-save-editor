DOCKER_IMAGE := "ff6-save-editor"
DOCKER_TAG := "dev"

lint:
    pre-commit run --all-files

test:
    poetry run pytest --verbosity=1

install:
    poetry install --sync

update: _poetry_lock install

docker-build:
    docker build --tag "{{ DOCKER_IMAGE }}:{{ DOCKER_TAG }}" .

_poetry_lock:
    poetry update --lock
