#!/usr/bin/env python

from mylib.calc import addition, subtract, multiply, divide
import click


@click.group()
def cli():
    """A simple calculator CLI."""


@cli.command()
@click.argument("x", type=float)
@click.argument("y", type=float)
def add(x, y):
    """Add two numbers.

    Example:
        ./calc-cli.py add 3 5
        Result: 8
    """
    # colored output
    result = addition(x, y)
    click.echo(click.style(f"Result: {result}", fg="green"))


@cli.command()
@click.argument("x", type=float)
@click.argument("y", type=float)
def sub(x, y):
    """Subtract two numbers.

    Example:
        ./calc-cli.py subtract 10 5
        Result: 5
    """
    result = subtract(x, y)
    click.echo(click.style(f"Result: {result}", fg="green"))


@cli.command()
@click.argument("x", type=float)
@click.argument("y", type=float)
def mult(x, y):
    """Multiply two numbers.

    Example:
        ./calc-cli.py multiply 3 5
        Result: 15
    """
    result = multiply(x, y)
    click.echo(click.style(f"Result: {result}", fg="green"))


@cli.command()
@click.argument("x", type=float)
@click.argument("y", type=float)
def div(x, y):
    """Divide two numbers.

    Example:
        ./calc-cli.py divide 10 2
        Result: 5.0
    """
    try:
        result = divide(x, y)
        click.echo(click.style(f"Result: {result}", fg="green"))
    except ValueError as e:
        click.echo(click.style(f"Error: {e}", fg="red"))


if __name__ == "__main__":
    cli()
