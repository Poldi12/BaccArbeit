import helpers
from pysat.formula import CNF
from pysat.solvers import Solver
from dataclasses_graph import *
# main function, checks, if given coloring is satisfiable
def af_SAT(NH_graph, max_color):

    CNF_list = []

    convert_graph_to_CNF(NH_graph, CNF_list)

    with Solver(bootstrap_with=CNF_list) as solver:

        if(solver.solve()):
            NH_graph.SAT = 1
        else:
            NH_graph.SAT = 0

    return 0

def convert_graph_to_CNF(NH_graph, CNF_list):

    

    return 0