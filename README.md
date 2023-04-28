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

Notice: When executing the program, you have to provide arguments when calling main for proper usage, for more infos call it with -help

One Option for Input Parameters in VSCode: use the provided launch.json file; select main.py -> select "Run and Debug" on left sidebar -> select "Start Debugging" on "Python:Current File"

## Structure

The "src" folder contains all relevant source files. The first of two main-parts is "generateNHgraph", which generates the Neighborhood Graph with a valid vertice coloring. The second is "ausgabefaerbung", which tries to color the generated graph with a new amount of colors(input defined) through a SAT-Solver. "dataclasses_graph" contains the data structure used in this project for the Neighborhood Graph and some Metadata. "validateNHgraph" validates the colors of the vertices after coloring them with the SAT Solver. "helpers" only prints the output to a file. An example can be found in "output.txt". "inputHandler" handles the input (you dont say).

The "bin" folder contains executable versions of the project (distinguished by the release date).

The "powershell" folder contains powershell skripts used for generating results for the thesis.

## Output

There are 2 output types: terminal and (optional) file.

The Terminal output and output.txt will give you information about the following:

Infos about the generated Graph:

* Max_color_Generate_Graph("m"): maximum color occuring in my_color and neighborhood_color, as well as the first coloring of the
* degree("d"): maximum number of neighbors, a node can have
* number_balls: amount of balls generated
* number total_adjacents: number of connections between balls 
* Runtime GenerateGraph: runtime, the function needed to complete the graph

Infos about the coloring(ausgabefaerbung) of the SATSolver:

* Solver: the selected type of solver for the SATSolver
* Max_color_Faerbung_input(q): maximum color, the solver tries to color the graph with
* Max_color_Solution: maximum color in the solution
* Number_of_CNF_clauses: amount of clauses generated for the solver
* SAT: if there exists a solution with that q
* Solution: the solution for all the balls, beginning with the first ball in "output-Graph.txt"
* Runtime Ausgabefaerbung: runtime, the function needed to complete
* Valid Solution: if the solution of the sat solver is valid for the graph (seperate check)

In between, you will also get some infos about the generated graph, number of cnf clauses generated and output coloring.

Depending if you set the input argument [?], there will be 1 or 3 output files. In the first, which will have the exact name as you specified in the [p] argument you passed. It will contain all the infos listed in the terminal regarding the graph and
output coloring.
The second file has "-Graph" attached to the output file name and contains the following detailed infos about the graph:

* mc: the value of "my color" of the node (combined with nc, they display the local view of a ball)
* nc: the values of the "neighbor colors" of the node 
* cba: the values of "my local view" of the adjacent balls
* number_adjacents: number of cba at this ball
* vertex_ausgabefaerbung: the current color of the ball

"-Graph2" shows infos of the Graph afte recoloring with "ausgabefaerbung" without the "cba" infos and with the recolored vertices(vertex_ausgabefaerbung), if the coloring was SAT. If it was not SAT, the vertices will have the same color as after generation.

## Misc for myself

todo

>