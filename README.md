# NHgraphColoring

The Purpose of this Python Project is to experiment with different Neighborhood Graphs and their vertice colorings.

## Table of Contents
* [Usage](#usage)
* [Setup Project](#setup-project)
* [Structure](#structure)
* [Misc for myself](#misc-for-myself)

## Usage

Python:

```
python BaccArbeit -help
```

Windows 11:

A compiled .exe files can be found within the "bin/" folder.
```
./main.exe -help
```

## Setup Project

```
pip install python-sat
pip install dataclasses
```

One Option for Input Parameters in VSCode: select main.py -> select "Run and Debug" on left sidebar -> select "Start Debugging" on "Python:Current File"

## Structure

The "src" folder contains all relevant source files. The first of two main-parts is "generateNHgraph", which generates the Neighborhood Graph with a valid vertice coloring. The second is "ausgabefaerbung", which tries to color the generated graph with a new amount of colors(input defined) through a SAT-Solver. "dataclasses_graph" contains the data structure used in this project for the Neighborhood Graph and some Metadata. "validateNHgraph" validates the colors of the vertices after coloring them with the SAT Solver. "helpers" only prints the output to a file. An example can be found in "output.txt".

## Misc for myself

todo: 

might do:
      >generate graph für max_color <= max_degree fixen
      >graphisches darstellen mit networkx?
      >färbung mit mehr als einer Runde?
      >Select Sat solver (glucose, ...) -> kein wirklicher Laufzeit-Unterschied festgestellt in ersten Tests
