# This is the main file calling the functions
import src.generateNHGraph as generateNHGraph
import src.helpers as helpers
import src.ausgabefaerbung as ausgabefaerbung
import src.dataclassesGraph as dataclassesGraph
import src.inputHandler as inputHandler

print("starting program...")
print()

# Variables
################

# "Errorhandler"
return_value = 0

#Instance of NHGraph
NH_graph_reference = dataclassesGraph.NHGraphC()

# Input parameters for generating graphs

input = dataclassesGraph.InputC()
return_value += inputHandler.handle_input(input)

# Call functions
################

if(return_value == 0):
    return_value += generateNHGraph.generate_NHGraph(input.m, input.d, NH_graph_reference)

if(return_value == 0):
    return_value += ausgabefaerbung.af_SAT(NH_graph_reference, input.q, input.Solver)

helpers.print_NHGraph(NH_graph_reference, input.m , input.d, input.q, input.PrintGraph, input.OutputFile, input.Output_Yes, input.Solver)

print("")
print("program finished")
#print("ret_val: " + str(return_value))