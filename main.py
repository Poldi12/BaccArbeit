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

'''
print_graph: bool = False
m: int = 6 #max input color
d: int = 3 #degree
ma: int = 5 #max output color (color for ausgabefaerbung)
file_name = 'output.txt'
'''

m = int(input("Enter maximum COLOR to generate Graph: "))
d = int(input("Enter maximum DEGREE to generate Graph: "))
ma = int(input("Enter maximum COLOR to color Graph: "))
file_name = input("Enter output file NAME (dont forget to add .txt for a text file): ")
print_graph = input("Write whole Graph to file? (y = yes, n = no): ")
print("")

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
    return_value += ausgabefaerbung.af_SAT(NH_graph_reference, ma)

helpers.print_NHGraph(NH_graph_reference, r, m , d, ma, print_graph, file_name)

print("")
print("program finished")
print("ret_val: " + str(return_value))