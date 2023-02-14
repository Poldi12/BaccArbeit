from pysat.solvers import Solver#, Cadical, Glucose3, Lingeling, MapleChrono, Minisat22
from src.dataclasses_graph import *
import time
import src.validateNHgraph as validateNHgraph

# main function, checks, if given coloring is satisfiable
def af_SAT(NH_graph, max_color):

    print("start coloring Graph...")
    
    st = time.process_time()

    solver = Solver()

    build_cnf_for_af(NH_graph, solver, max_color)

    NH_graph.NOC = solver.nof_clauses()

    if(solver.solve()):
        NH_graph.SAT = 1
        NH_graph.Solution = decode_position_with_color(solver.get_model(), max_color)
        assign_new_color_values(NH_graph, NH_graph.Solution)
        validateNHgraph.validation(NH_graph)
    else:
        NH_graph.SAT = 0
        NH_graph.Problem = solver.get_core()

    solver.delete()

    et = time.process_time()

    NH_graph.LaufzeitAusgabefärbung = et - st

    print("coloring Graph finished")

    return 0

def build_cnf_for_af(NH_graph, solver, max_color):

    #Neighbor not same color (-a1v-b1 -a2v-b2 ...)
    for vertice in range(len(NH_graph.VerticeList)):
        for adjacent in range(len(NH_graph.VerticeList[vertice].Ball.Adjacents)):

            adjacent_position_in_vertice_list = NH_graph.VerticeList[vertice].Ball.Adjacents[adjacent].PositionInVerticeList

            for color in range(1, max_color+1):

                vertice_enc = encode_position_with_color(vertice, color, max_color)
                adjacent_enc = encode_position_with_color(adjacent_position_in_vertice_list, color, max_color)
                solver.add_clause([-vertice_enc, -adjacent_enc])

    #Every node needs a color (a1va2va3)
    for vertice in range(len(NH_graph.VerticeList)):
        cnf_list: int = []
        for color in range(1, max_color +1):
            cnf_list.append(encode_position_with_color(vertice, color, max_color))
        solver.add_clause(cnf_list)

    #Only 1 color per node (-a1v-a2 -a1v-a3 -a2v-a3)
        for color in range(1, max_color+1):
            for color2 in range(color +1,max_color+1):

                vertice_enc1 = encode_position_with_color(vertice, color, max_color)
                vertice_enc2 = encode_position_with_color(vertice, color2, max_color)

                solver.add_clause([-vertice_enc1, -vertice_enc2])
            


def encode_position_with_color(variable, color, max_color):

    #first part is position in VerticeList, second is color
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

    for vertice in range(len(NH_graph.VerticeList)):
        NH_graph.VerticeList[vertice].AF = ball_color_tuple[vertice]

    return 0
