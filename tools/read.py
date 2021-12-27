# -*- coding: utf-8 -*-
# Author: michalspano
# Pascal's Triangle with graphical interface
# Read from a raw `.gv` file

from graphviz import Source
from tools.time_it import timeit


@timeit
def readGV(path: str, viewGraph: bool = True) -> bool:
    try:
        Source.from_file(path, format='png').render(path, view=viewGraph)
    except FileNotFoundError or ImportError:
        return False
    return True
