import helpers
from pysat.formula import CNF
from pysat.solvers import Solver
from dataclasses_graph import *
import time

# main function, checks, if given coloring is satisfiable
def af_SAT(NH_graph, max_color):
    
    st = time.process_time()

    solver = Solver()

    build_cnf_for_af(NH_graph, solver, max_color)

    print(str(solver.nof_clauses()))

    if(solver.solve()):
        NH_graph.SAT = 1
        NH_graph.Solution = solver.get_model()
    else:
        NH_graph.SAT = 0
        NH_graph.Problem = solver.get_core()
        print(str(solver.get_core()))

    et = time.process_time()

    NH_graph.LaufzeitAusgabefärbung = et - st

    return 0

def build_cnf_for_af(NH_graph, solver, max_color):

    #Neighbor not same color (-a1v-b1 -a2v-b2 ...)
    for vertice in range(len(NH_graph.VerticeList)):
        for adjacent in range(len(NH_graph.VerticeList[vertice].Ball.Adjacents)):

            adjacent_position_in_vertice_list = NH_graph.VerticeList[vertice].Ball.Adjacents[adjacent].PositionInVerticeList

            for color in range(1,max_color+1):

                vertice_enc = encode_position_with_color(vertice, color)
                adjacent_enc = encode_position_with_color(adjacent_position_in_vertice_list, color)
                #print(str(-vertice_enc))
                solver.add_clause([-vertice_enc, -adjacent_enc])

    #Every node needs a color (a1va2va3)
        #i know its ugly, but pysat does not allow addin dynamic cnf clauses
        match max_color:
            case 1:
                vertice_enc1 = encode_position_with_color(vertice, 1)
                solver.add_clause([vertice_enc1])

            case 2:
                vertice_enc1 = encode_position_with_color(vertice, 1)
                vertice_enc2 = encode_position_with_color(vertice, 2)
                solver.add_clause([vertice_enc1, vertice_enc2])

            case 3:
                vertice_enc1 = encode_position_with_color(vertice, 1)
                vertice_enc2 = encode_position_with_color(vertice, 2)
                vertice_enc3 = encode_position_with_color(vertice, 3)
                solver.add_clause([vertice_enc1, vertice_enc2, vertice_enc3])

            case 4:
                vertice_enc1 = encode_position_with_color(vertice, 1)
                vertice_enc2 = encode_position_with_color(vertice, 2)
                vertice_enc3 = encode_position_with_color(vertice, 3)
                vertice_enc4 = encode_position_with_color(vertice, 4)
                solver.add_clause([vertice_enc1, vertice_enc2, vertice_enc3, vertice_enc4])

            case 5:
                vertice_enc1 = encode_position_with_color(vertice, 1)
                vertice_enc2 = encode_position_with_color(vertice, 2)
                vertice_enc3 = encode_position_with_color(vertice, 3)
                vertice_enc4 = encode_position_with_color(vertice, 4)
                vertice_enc5 = encode_position_with_color(vertice, 5)
                solver.add_clause([vertice_enc1, vertice_enc2, vertice_enc3, vertice_enc4, vertice_enc5])

            case 6:
                vertice_enc1 = encode_position_with_color(vertice, 1)
                vertice_enc2 = encode_position_with_color(vertice, 2)
                vertice_enc3 = encode_position_with_color(vertice, 3)
                vertice_enc4 = encode_position_with_color(vertice, 4)
                vertice_enc5 = encode_position_with_color(vertice, 5)
                vertice_enc6 = encode_position_with_color(vertice, 6)
                solver.add_clause([vertice_enc1, vertice_enc2, vertice_enc3, vertice_enc4, vertice_enc5, vertice_enc6])
            
            case 7:
                vertice_enc1 = encode_position_with_color(vertice, 1)
                vertice_enc2 = encode_position_with_color(vertice, 2)
                vertice_enc3 = encode_position_with_color(vertice, 3)
                vertice_enc4 = encode_position_with_color(vertice, 4)
                vertice_enc5 = encode_position_with_color(vertice, 5)
                vertice_enc6 = encode_position_with_color(vertice, 6)
                vertice_enc7 = encode_position_with_color(vertice, 7)
                solver.add_clause([vertice_enc1, vertice_enc2, vertice_enc3, vertice_enc4, vertice_enc5, vertice_enc6, vertice_enc7])

            case 8:
                vertice_enc1 = encode_position_with_color(vertice, 1)
                vertice_enc2 = encode_position_with_color(vertice, 2)
                vertice_enc3 = encode_position_with_color(vertice, 3)
                vertice_enc4 = encode_position_with_color(vertice, 4)
                vertice_enc5 = encode_position_with_color(vertice, 5)
                vertice_enc6 = encode_position_with_color(vertice, 6)
                vertice_enc7 = encode_position_with_color(vertice, 7)
                vertice_enc8 = encode_position_with_color(vertice, 8)
                solver.add_clause([vertice_enc1, vertice_enc2, vertice_enc3, vertice_enc4, vertice_enc5, vertice_enc6, vertice_enc7, vertice_enc8])
            
            case 9:
                vertice_enc1 = encode_position_with_color(vertice, 1)
                vertice_enc2 = encode_position_with_color(vertice, 2)
                vertice_enc3 = encode_position_with_color(vertice, 3)
                vertice_enc4 = encode_position_with_color(vertice, 4)
                vertice_enc5 = encode_position_with_color(vertice, 5)
                vertice_enc6 = encode_position_with_color(vertice, 6)
                vertice_enc7 = encode_position_with_color(vertice, 7)
                vertice_enc8 = encode_position_with_color(vertice, 8)
                vertice_enc9 = encode_position_with_color(vertice, 9)
                solver.add_clause([vertice_enc1, vertice_enc2, vertice_enc3, vertice_enc4, vertice_enc5, vertice_enc6, vertice_enc7, vertice_enc8, vertice_enc9])

    #Only 1 color per node (-a1v-a2 -a1v-a3 -a2v-a3)
        for color in range(1, max_color+1):
            for color2 in range(color +1,max_color+1):

                vertice_enc1 = encode_position_with_color(vertice, color)
                vertice_enc2 = encode_position_with_color(vertice, color2)

                solver.add_clause([vertice_enc1, vertice_enc2])
            


def encode_position_with_color(variable, color):

    #first part is position in VerticeList, second is color
    result = str(variable) + str(color)
    return int(result)
