import click


@click.command()
def hello():
    print("Hello physicist!")

if __name__ == "__main__":
    hello()
