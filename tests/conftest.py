import pytest
from fastapi.testclient import TestClient
from copy import deepcopy
from src.app import app, activities


@pytest.fixture
def client():
    """Fixture that provides a TestClient with isolated activity state"""
    # Store original activities
    original_activities = deepcopy(activities)
    
    # Yield the client for tests
    yield TestClient(app)
    
    # Restore original activities after test
    activities.clear()
    activities.update(original_activities)
