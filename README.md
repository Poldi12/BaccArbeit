# NHgraphColoring

The Purpose of this Python Project is to experiment with different Neighborhood Graphs and their vertice colorings.

## Table of Contents
* [Usage](#usage)
* [Setup Project](#setup-project)
* [Structure](#structure)
* [Output](#output)
* [Misc for myself](#misc-for-myself)

## Usage

Python:

```
python BaccArbeit -help
```

Windows 11:

A compiled .exe files can be found within the "bin/" folder.
```
.\main.exe -help
```

## Setup Project

```
pip install python-sat
pip install dataclasses
```

One Option for Input Parameters in VSCode: select main.py -> select "Run and Debug" on left sidebar -> select "Start Debugging" on "Python:Current File"

## Structure

The "src" folder contains all relevant source files. The first of two main-parts is "generateNHgraph", which generates the Neighborhood Graph with a valid vertice coloring. The second is "ausgabefaerbung", which tries to color the generated graph with a new amount of colors(input defined) through a SAT-Solver. "dataclasses_graph" contains the data structure used in this project for the Neighborhood Graph and some Metadata. "validateNHgraph" validates the colors of the vertices after coloring them with the SAT Solver. "helpers" only prints the output to a file. An example can be found in "output.txt". "inputHandler" handles the input (you dont say).

## Output

There are 2 output types: terminal and (optional) file.

The Terminal output will give you information about the progress of the graph generation and output coloring. In between, you will also get some infos about the generated graph, number of cnf clauses generated and output coloring.

Depending if you set the input argument [?], there will be 1 or 2 output files. In the first, which will have the exact name as you specified in the [p] argument you passed. It will contain all the infos listed in the terminal regarding the graph and
output coloring.
The second file have "-Graph" attached to the output file name and contain the graph itself.

## Misc for myself

todo: duplicate im generate herausfiltern (als 2. option angeben, original auch drinnen lassen)
      output print variable names according to naming convention used in paper
      

might do:
      >graphisches darstellen mit networkx?
      >färbung mit mehr als einer Runde?
