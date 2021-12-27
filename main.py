#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: michalspano
# Pascal's Triangle with graphical interface

# Module imports
import graphviz as gv
from sys import argv, exit
from tools.read import readGV
from datetime import datetime


# Create the main function with default operations
def main(numberOfRows: int = 10, enableGraph: bool = False, debug: bool = False, outPath: str = './out/') -> None:
    # Check proper number of rows
    if numberOfRows < 1:
        print('The number of rows must be greater than 1.')
        exit(1)

    # Check for any optional flags
    # The order of the flags is not important
    if len(argv) != 1:
        # Skip the base name of the script
        for arg in argv[1:]:

            # Graph flag - enables the graph
            if arg == '--graph' or arg == '-g':
                enableGraph = True

            # Debug flag - enables the debug mode
            elif arg == '--debug' or arg == '-d':
                debug = True

            # Read flag - reads the graph from a file of type '.gv'
            elif arg == '--read' or arg == '-r':
                if not readGV(path=f'{outPath}Graph.gv', viewGraph=True):
                    print("Error reading and/or processing the graph")
                    exit(1)
                # End the call
                exit(0)
            else:
                # Detect any undefined flags
                print('Unknown argument: ' + arg)
                exit(1)

    # Debug time initialised
    start = datetime.now()

    # Structure to store the Pascal's triangle
    # Type: list of lists of integers
    pascalTriangle: list = [[1]]  # <- Initial row

    # Compose the Pascal's triangle
    for i in range(1, numberOfRows + 1):
        currentRow: list = [1]
        for j in range(1, i):
            currentRow.append(pascalTriangle[i - 1][j - 1] + pascalTriangle[i - 1][j])
        currentRow.append(1)
        # Append new row
        pascalTriangle.append(currentRow)

    # Default behaviour, no graphical output
    if not enableGraph:
        for idx in enumerate(pascalTriangle):
            print(' ' * (numberOfRows + 1 - idx[0]), idx[1])
        if debug:
            print(f'Time elapsed: {datetime.now() - start}')
        exit(0)

    # Instantiate the graph object
    dot = gv.Graph(format='png')

    # Create a hash function that will be used to create unique names for the nodes
    def hash_function(node_idx: list) -> str:
        return f"n{'-'.join(str(x) for x in node_idx)}"

    for i in range(len(pascalTriangle)):
        # Head of the Pascal's Triangle
        if i == 0:
            # Create the 'HEAD' node
            dot.node(hash_function([0, 0]), str(pascalTriangle[i][0]))
            continue

        # Compute the general case
        for j in range(len(pascalTriangle[i])):
            # Create the nodes
            dot.node(hash_function([i, j]), str(pascalTriangle[i][j]))

        # Create the edges of each row
        for k in range(len(pascalTriangle[i - 1])):
            dot.edge(hash_function([i - 1, k]), hash_function([i, k]))
            dot.edge(hash_function([i - 1, k]), hash_function([i, k + 1]))

    # Render the graph
    dot.render(directory=outPath, filename='Graph.gv', view=True)

    # Debug mode enabled
    if debug:
        print(f'Debug: {dot.source}\n')
        print(f'Time elapsed: {datetime.now() - start}')


# Invoke the main function
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted by user')
