# This is the main file to start the program

import src.generateNHGraph as generateNHGraph
import src.helpers as helpers
import src.ausgabefaerbung as ausgabefaerbung
import src.dataclassesGraph as dataclassesGraph
import src.inputHandler as inputHandler

print("starting program...")
print()

# "Errorhandler"
return_value = 0

#Instance of NHGraph
NH_graph_reference = dataclassesGraph.NHGraphC()

# Input parameters for generating graphs
input = dataclassesGraph.InputC()

# Call functions
################

return_value += inputHandler.handle_input(input)

if(return_value == 0):
    return_value += generateNHGraph.generate_NHGraph(input.m, input.d, NH_graph_reference)

if(return_value == 0):
    return_value += ausgabefaerbung.af_SAT(NH_graph_reference, input.q, input.Solver)

if(return_value == 0):
    helpers.print_NHGraph(NH_graph_reference, input.m , input.d, input.q, input.PrintGraph, input.OutputFile, input.Solver)

print("")
print("program finished")
#print("ret_val: " + str(return_value))