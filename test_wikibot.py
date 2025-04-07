from mylib.bot import scrape
from click.testing import CliRunner
from wikibot import cli

def test_scrape():
    assert "Microsoft" in scrape("Microsoft")

#test the cli

def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ['--name', 'Microsoft'])
    assert result.exit_code == 0
    assert "Summary of Microsoft:" in result.output
