# This is the main file calling the functions

import generate_graph
import color_graph_networkx

print("starting program...")

r: int = 1 #later change to input{"Enter rounds:"}
m: int = 3
d: int = 2

return_value = 0

if(return_value == 0):
    return_value += generate_graph.generateNeighborhoodGraph(r, m, d)

"""
if(return_value == 0):
    color_graph_networkx.colorGraph()
"""

#print("ret_val: " + str(return_value))