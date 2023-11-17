import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def sin_tan_group():
    pass

@sin_tan_group.command()
@click.option(
    "-n",
    "--number",
    default=1,
    help="Value we put in sine.",
    show_default=True,  # show default in help
)

def sin(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

@sin_tan_group.command()
@click.option(
    "-n",
    "--number",
    default=1,
    help="Value we put in tan.",
    show_default=True,  # show default in help
)

def tan(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return

if __name__ == "__main__":
    sin_tan_group()