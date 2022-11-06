# This is the main file calling the functions

import generate_graph
import color_graph_networkx

print("starting program...")

# "Errorhandler"
return_value = 0

# Input parameters for generating graphs
r: int = 1 #rounds #later change to input{"Enter rounds:"}
m: int = 3 #max color
d: int = 2 #degree

if (d >= m):
        print("invalid input for generating valid Neighbourhoodgraph\n (Check max degree and number of colors input)")
        return_value += 1

# Nested list containing generated graphs
all_balls_list = []

# Call functions
################

if(return_value == 0):
    return_value += generate_graph.generateNeighborhoodGraph(r, m, d, all_balls_list)

"""
if(return_value == 0):
    return_value += color_graph_networkx.ausgabefaerbung(all_balls_list):
"""

#print("ret_val: " + str(return_value))