# This is the main file calling the functions
import generate_NH_graph
import helpers
import ausgabefaerbung

print("starting program...")
print("")

# Variables
################

# "Errorhandler"
return_value = 0

#points to NH_Graph
NH_graph_reference = [] 

# Input parameters for generating graphs
r: int = 1 #rounds #later change to input{"Enter rounds:"}
m: int = 4 #max color
d: int = 3 #degree

if (d >= m):
        print("invalid input for generating valid Neighbourhoodgraph\n (Check max degree and number of colors input)")
        return_value += 1


# Call functions
################

if(return_value == 0):
    return_value += generate_NH_graph.generateNeighborhoodGraph(r, m, d, NH_graph_reference)

"""
if(return_value == 0):
    return_value += ausgabefaerbung.af_first(NH_graph_reference, m)
"""
print("")
print("ret_val: " + str(return_value))