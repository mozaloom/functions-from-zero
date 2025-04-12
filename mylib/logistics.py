"""
this module deals with logistics operations adn calculates distance between two points
and the time taken to travel between them and other logistics related operations

example usage:
print(calculate_distance("New York", "Los Angeles"))

"""
import geopy
from geopy.distance import great_circle

#build a list of 10 cities with their coordinates
cities = [
    {"name": "New York", "coordinates": (40.7128, -74.0060)},
    {"name": "Los Angeles", "coordinates": (34.0522, -118.2437)},
    {"name": "Chicago", "coordinates": (41.8781, -87.6298)},
    {"name": "Houston", "coordinates": (29.7604, -95.3698)},
    {"name": "Phoenix", "coordinates": (33.4484, -112.0740)},
    {"name": "Philadelphia", "coordinates": (39.9526, -75.1652)},
    {"name": "San Antonio", "coordinates": (29.4241, -98.4936)},
    {"name": "San Diego", "coordinates": (32.7157, -117.1611)},
    {"name": "Dallas", "coordinates": (32.7767, -96.7970)},
    {"name": "San Jose", "coordinates": (37.3382, -121.8863)}
]

def calculate_distance(coords_1, coords_2):
    """
    Calculate the distance between two sets of coordinates.
    """
    return great_circle(coords_1, coords_2).miles


def find_coordinates(city_name):
    """
    Find the coordinates of a city by its name.
    """
    for city in cities:
        if city["name"].lower() == city_name.lower():
            return city["coordinates"]
    return None


def total_distance(cities_list):
    """
    Calculate the total distance of a route defined by a list of city names.
    """
    total_dist = 0
    for i in range(len(cities_list) - 1):
        city1 = find_coordinates(cities_list[i])
        city2 = find_coordinates(cities_list[i + 1])
        if city1 and city2:
            total_dist += calculate_distance(city1, city2)
    return total_dist

def find_distance(city1_name, city2_name):
    """
    Find the distance between two cities by their names.
    
    """
    cord1 = find_coordinates(city1_name)
    cord2 = find_coordinates(city2_name)
    if cord1 and cord2:
        return calculate_distance(cord1, cord2)
    else:
        return None

