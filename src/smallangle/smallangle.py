# Femke van Balen 14004089
# 17-11-2023
# Programme that calculates either the sin or the tangent,
# including the usage of click.
# ! I purposely did not use comments, because of the usage of docstrings ! (asked a TA)
import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def sin_tan_group():
    """This function puts the sine and tangent together in 1 group. It is now possible to
    call either sin or tan, using seperate commands.
    """
    pass

help(sin_tan_group)

@sin_tan_group.command()
@click.option(
    "-n",
    "--number",
    default=1,
    help="Value we put in sine.",
    show_default=True,  
)

def sin(number):
    """This function calculates the value of the sine for 'n' steps, between 0 and 2pi.
    You can choose a specific value for n by typing it in the terminal using the click writing format.

    Args:
        number (_type_): int
    
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

help(sin)

@sin_tan_group.command()
@click.option(
    "-n",
    "--number",
    default=1,
    help="Value we put in tan.",
    show_default=True,  
)

def tan(number):
    """This function calculates the value of the tangent for 'n' steps, between 0 and 2pi.
    You can choose a specific value for n by typing it in the terminal using the click writing format.

    Args:
        number (_type_): int
    """
    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return

help(tan)

if __name__ == "__main__":
    sin_tan_group()