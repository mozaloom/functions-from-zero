from mylib.bot import scrape
import click

@click.command()
@click.option('--name', prompt='Wikipedia page name',
              help='The name of the Wikipedia page to scrape.')
@click.option('--length', default=1, help='Number of sentences to scrape.')

def cli(name="Microsoft", length=1):
    result = scrape(name, length=length)           
    click.echo(click.style(f"Summary of {name}: {result}",bg='white', fg='green'))


if __name__ == '__main__':
    cli()
