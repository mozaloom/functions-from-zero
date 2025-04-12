#!/usr/bin/env python
import click
from mylib.logistics import find_coordinates, total_distance, find_distance, cities


@click.group()
def cli():
    """A simple logistics CLI."""


@cli.command()  # print the list of cities
def list_cities():
    """List all available cities.

    Example:
        ./logisticsCli.py list_cities
        Result: New York, Los Angeles, Chicago, Houston, Phoenix, Philadelphia, San Antonio, San Diego, Dallas, San Jose
    """
    city_names = [city["name"] for city in cities]
    click.echo(click.style(", ".join(city_names), fg="green"))


@cli.command()
@click.argument("city1")
@click.argument("city2")
def distance(city1, city2):
    """Calculate the distance between two cities.

    Example:
        ./logisticsCli.py distance "New York" "Los Angeles"
        Result: 2451.0 miles
    """
    result = find_distance(city1, city2)
    click.echo(click.style(f"Distance: {result} miles", fg="green"))


@cli.command()
@click.argument("city1")
@click.argument("city2")
def route_distance(city1, city2):
    """Calculate the distance of a route between two cities.

    Example:
        ./logisticsCli.py route_distance "New York" "Los Angeles"
        Result: 2451.0 miles
    """
    result = total_distance([city1, city2])
    click.echo(click.style(f"Route Distance: {result} miles", fg="green"))


@cli.command()
@click.argument("city_name")
def coordinates(city_name):
    """Find the coordinates of a city.

    Example:
        ./logisticsCli.py coordinates "New York"
        Result: (40.7128, -74.0060)
    """
    result = find_coordinates(city_name)
    if result:
        click.echo(click.style(f"Coordinates: {result}", fg="green"))
    else:
        click.echo(click.style("City not found", fg="red"))


if __name__ == "__main__":
    cli()
