from mylib.calc import addition, subtract, multiply, divide, power
from calcCli import cli
import click


def test_addition():
    assert addition(2, 3) == 5


def test_subtraction():
    assert subtract(5, 3) == 2


def test_multiplication():
    assert multiply(2, 3) == 6


def test_division():
    assert divide(6, 3) == 2
    try:
        divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"


def test_power():
    assert power(2, 3) == 8


# writ e a test for the cli command
def test_cli_addition():
    runner = click.testing.CliRunner()
    result = runner.invoke(cli, ["add", "2", "3"])
    assert result.exit_code == 0
    assert "Result: 5" in result.output


def test_cli_subtraction():
    runner = click.testing.CliRunner()
    result = runner.invoke(cli, ["sub", "5", "3"])
    assert result.exit_code == 0
    assert "Result: 2" in result.output


def test_cli_multiplication():
    runner = click.testing.CliRunner()
    result = runner.invoke(cli, ["mult", "2", "3"])
    assert result.exit_code == 0
    assert "Result: 6" in result.output


def test_cli_division():
    runner = click.testing.CliRunner()
    result = runner.invoke(cli, ["div", "6", "3"])
    assert result.exit_code == 0
    assert "Result: 2.0" in result.output
