import click 
import time


@click.command()
@click.argument("name")
@click.option(
    "-c",
    "--count",
    default=1,
    help="Number of times to print greeting.",
    show_default=True,  # show default in help
)
@click.option(
    "-t",
    "--time_pause",
    default=0.0,
    help="A time pause between print statements",
    show_default = True
)

def hello(name, count, time_pause):
    for _ in range(count):
        print(f"Hello {name}!")
        time.sleep(time_pause)
    

if __name__ == "__main__":
    hello()
