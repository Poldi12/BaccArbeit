# This is the main file calling the functions
import src.generateNHgraph as generateNHgraph
import src.helpers as helpers
import src.ausgabefaerbung as ausgabefaerbung
import src.dataclasses_graph as dataclasses_graph
import sys

print("starting program...")
print()

# Variables
################

# "Errorhandler"
return_value = 0

#points to NH_Graph
NH_graph_reference = dataclasses_graph.NHGraphC()

# Input parameters for generating graphs

r: int = 1 #rounds #later change to input{"Enter rounds:"}

'''
print_graph: bool = False
m: int = 6 #max input color
d: int = 3 #degree
ma: int = 5 #max output color (color for ausgabefaerbung)
file_name = 'output.txt'
print_graph = False
'''

if(sys.argv[1] == '-help'):
    
    print("Input Parameters:")
    print("#################")
    print()
    print("m = maximum color for generating graph")
    print("d = degree/ maximum number of neighbors, a node can have")
    print("q = maximum color to color the graph with, after generating the graph")
    print("p = path and filename to store the output (example: C:/output/output.txt)")
    print("? = print the whole graph? possible inputs 'y'=yes, 'n'=no ")
    print()
    print("./main.exe [m] [d] [q] [p] [?]")
    print()
    input("Press ENTER to exit program")
    sys.exit()

m = int(sys.argv[1])
d = int(sys.argv[2])
q = int(sys.argv[3])
file_name = sys.argv[4]
print_graph = sys.argv[5]

if(print_graph == 'n'):
    print_graph = False

if (d >= m):
    print("invalid input for generating valid Neighbourhoodgraph\n (Check max degree and number of colors input)")
    return_value += 1

# Call functions
################

if(return_value == 0):
    return_value += generateNHgraph.generate_NHGraph(m, d, NH_graph_reference)

if(return_value == 0):
    return_value += ausgabefaerbung.af_SAT(NH_graph_reference, q)

helpers.print_NHGraph(NH_graph_reference, r, m , d, q, print_graph, file_name)

print("")
print("program finished")
print("ret_val: " + str(return_value))