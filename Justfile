lint:
    pre-commit run --all-files

test:
    poetry run pytest \
      --verbosity=1 \
      --cov --cov-append \
      --cov-report=term-missing:skip-covered \
      --cov-fail-under=98

install:
    poetry install --sync

update: _poetry_lock install

_poetry_lock:
    poetry update --lock
