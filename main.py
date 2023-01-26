# This is the main file calling the functions
import generateNHgraph
import helpers
import ausgabefaerbung
import dataclasses_graph

print("starting program...")
print("")

# Variables
################

# "Errorhandler"
return_value = 0

#points to NH_Graph
NH_graph_reference = dataclasses_graph.NHGraphC()

# Input parameters for generating graphs
r: int = 1 #rounds #later change to input{"Enter rounds:"}
m: int = 3 #max color (color from 1-9 are valid)
d: int = 2 #degree

if (d >= m):
        print("invalid input for generating valid Neighbourhoodgraph\n (Check max degree and number of colors input)")
        return_value += 1


# Call functions
################

if(return_value == 0):
    return_value += generateNHgraph.generate_NHGraph(r, m, d, NH_graph_reference)


if(return_value == 0):
    return_value += ausgabefaerbung.af_SAT(NH_graph_reference, m)

helpers.print_NHGraph(NH_graph_reference)

print("")
print("ret_val: " + str(return_value))