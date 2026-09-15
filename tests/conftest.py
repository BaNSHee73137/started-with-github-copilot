import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture
def client(monkeypatch):
    activities = copy.deepcopy(app_module.activities)
    monkeypatch.setattr(app_module, "activities", activities)

    with TestClient(app_module.app) as test_client:
        yield test_client