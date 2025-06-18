lint:
    pre-commit run --all-files

test:
    poetry run pytest --verbosity=1

install:
    poetry sync

update: _poetry_lock install

_poetry_lock:
    poetry update --lock
