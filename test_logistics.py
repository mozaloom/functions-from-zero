from mylib.logistics import (
    find_coordinates,
    total_distance,
    find_distance,
)


def test_find_coordinates():
    assert find_coordinates("New York") == (40.7128, -74.0060)


def test_find_distance():
    assert find_distance("New York", "Los Angeles") == 2445.5627972925


def test_total_distance():
    assert total_distance(["New York", "Los Angeles"]) == 2445.5627972925
