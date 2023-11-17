import click 


@click.command()
@click.argument("name")
@click.option(
    "-c",
    "--count",
    default=1,
)

def hello(name, count):
    for _ in range(count):
        print(f"Hello {name}!")
    

if __name__ == "__main__":
    hello()
