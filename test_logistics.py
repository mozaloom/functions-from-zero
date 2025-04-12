from fastapi.testclient import TestClient
from mylib.logistics import (
    find_coordinates,
    total_distance,
    find_distance,
)

from mainLogistics import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello FastAPI Logistics"}


def test_cities():
    response = client.get("/cities")
    assert response.status_code == 200
    assert "cities" in response.json()
    assert isinstance(response.json()["cities"], list)
    assert len(response.json()["cities"]) > 0


def test_distance():
    response = client.post(
        "/distance",
        json={"city1": "New York", "city2": "Los Angeles"},
    )
    assert response.status_code == 200
    assert "distance" in response.json()
    assert isinstance(response.json()["distance"], float)


def test_travel_time():
    response = client.post(
        "/travel_time",
        json={"city1": "New York", "city2": "Los Angeles"},
    )
    assert response.status_code == 200
    assert "travel_time" in response.json()
    assert isinstance(response.json()["travel_time"], float)


def test_find_coordinates():
    assert find_coordinates("New York") == (40.7128, -74.0060)


def test_find_distance():
    assert find_distance("New York", "Los Angeles") == 2445.5627972925


def test_total_distance():
    assert total_distance(["New York", "Los Angeles"]) == 2445.5627972925
