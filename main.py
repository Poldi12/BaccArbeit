# This is the main file calling the functions
import generateNHgraph
import helpers
import ausgabefaerbung
import dataclasses_graph
import validateNHgraph

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
m: int = 4 #max input color
d: int = 3 #degree

ma: int = 5 #max output color (color for ausgabefaerbung)

'''
if (d >= m):
        print("invalid input for generating valid Neighbourhoodgraph\n (Check max degree and number of colors input)")
        return_value += 1
'''

# Call functions
################

if(return_value == 0):
    return_value += generateNHgraph.generate_NHGraph(m, d, NH_graph_reference)

if(return_value == 0):
    return_value += ausgabefaerbung.af_SAT(NH_graph_reference, ma)

if(return_value == 0):
    return_value += validateNHgraph.validation(NH_graph_reference)

helpers.print_NHGraph(NH_graph_reference, r, m , d, ma)

print("")
print("ret_val: " + str(return_value))