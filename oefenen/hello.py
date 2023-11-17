import click 


@click.command()
@click.argument("name")
@click.option(
    "-c",
    "--count",
    default=1,
)
def hello(name):
    print(f"Hello {name}!")
    

if __name__ == "__main__":
    hello()
