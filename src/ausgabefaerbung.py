#This file contains all functionality regarding coloring the graph after generation

from pysat.solvers import Solver
from src.dataclassesGraph import *
import time
import src.validateNHGraph as validateNHGraph

def af_SAT(NH_graph, max_color, solver_selected):

    print("start coloring Graph...")
    
    st = time.process_time()

    #Solver is selected
    solver = Solver(name = solver_selected)
    
    #cnf is generated
    build_cnf_for_af(NH_graph, solver, max_color)

    #get number of cnf clauses
    NH_graph.NOC = solver.nof_clauses()
    print('number of cnf clauses: ' + str(solver.nof_clauses()))
    
    print("solving...")

    #Try to solve the graph
    if(solver.solve()):
        NH_graph.SAT = 1
        NH_graph.Solution = decode_position_with_color(solver.get_model(), max_color)

        #map new colors to graph and validate them
        assign_new_color_values(NH_graph, NH_graph.Solution)
        validateNHGraph.validation(NH_graph)
    else:
        NH_graph.SAT = 0

    solver.delete()

    et = time.process_time()
    NH_graph.LaufzeitAusgabefärbung = et - st

    print("coloring Graph finished")

    return 0

def build_cnf_for_af(NH_graph, solver, max_color):

    #Neighbor not same color (-a1v-b1 -a2v-b2 ...)
    for vertex in range(len(NH_graph.vertexList)):
        for adjacent in range(len(NH_graph.vertexList[vertex].Ball.Adjacents)):

            adjacent_position_in_vertex_list = NH_graph.vertexList[vertex].Ball.Adjacents[adjacent].PositionInvertexList

            for color in range(1, max_color+1):

                vertex_enc = encode_position_with_color(vertex, color, max_color)
                adjacent_enc = encode_position_with_color(adjacent_position_in_vertex_list, color, max_color)
                solver.add_clause([-vertex_enc, -adjacent_enc])

    #Every node needs a color (a1va2va3)
    for vertex in range(len(NH_graph.vertexList)):
        cnf_list: int = []
        for color in range(1, max_color +1):
            cnf_list.append(encode_position_with_color(vertex, color, max_color))
        solver.add_clause(cnf_list)

    #Only 1 color per node (-a1v-a2 -a1v-a3 -a2v-a3)
        for color in range(1, max_color+1):
            for color2 in range(color +1,max_color+1):

                vertex_enc1 = encode_position_with_color(vertex, color, max_color)
                vertex_enc2 = encode_position_with_color(vertex, color2, max_color)

                solver.add_clause([-vertex_enc1, -vertex_enc2])
            


def encode_position_with_color(variable, color, max_color):

    #first part is position in vertexList, second is color
    result = variable*max_color + color
    return int(result)

def decode_position_with_color(list, max_color):

    ball_color_tuple = []
    for entry in range(len(list)):
        if (list[entry] < 0): continue
        else:
            #position = list[entry] / max_color #not exact
            color = 1+(list[entry] % max_color)
            ball_color_tuple.append(color)
            
    return ball_color_tuple

def assign_new_color_values(NH_graph, ball_color_tuple):

    for vertex in range(len(NH_graph.vertexList)):
        NH_graph.vertexList[vertex].AF = ball_color_tuple[vertex]

    return 0
