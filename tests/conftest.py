from time import time

import pytest


@pytest.fixture(autouse=True)
def faker_seed() -> float:
    return time()
