import networkx
import matplotlib.pyplot as plt
from enum import Enum
from dataclasses_graph import *

#print networkx, currently not in use
def print_networkx(all_balls_list, position):

    print_ball = all_balls_list[position]
    networkx.draw_networkx(print_ball, with_labels=True)

    ax = plt.gca()
    ax.margins(0.10)
    plt.axis("on")
    plt.show()

def print_NHGraph(NHGraph, r, m , d, ma, print_graph, file_name):

    file = open(file_name, 'w')

    if(print_graph):
        for i in range(len(NHGraph.VerticeList)):

            # ball with mc and ncs
            file.write('mc: ' + str(NHGraph.VerticeList[i].Ball.MyLocalView.MyColor) + '\n nc: ')
            for j in range(len(NHGraph.VerticeList[i].Ball.MyLocalView.NeighborColors)):
                file.write(str(NHGraph.VerticeList[i].Ball.MyLocalView.NeighborColors[j]) + ' ')
            file.write('\n')

            # possible adjacents 
            for k in range(len(NHGraph.VerticeList[i].Ball.Adjacents)):
                current_adjacent_view = NHGraph.VerticeList[i].Ball.Adjacents[k].Ball.MyLocalView
                file.write(' cba mc: ' + str(current_adjacent_view.MyColor) + ' nc: ')
                for j in range(len(current_adjacent_view.NeighborColors)):
                    file.write(str(current_adjacent_view.NeighborColors[j]) + ' ')
                file.write('\n')
            file.write('number_adjacents:' + str(len(NHGraph.VerticeList[i].Ball.Adjacents)))
            file.write('\n')

            # vertices
            file.write('vertice_ausgabefaerbung:' + str(NHGraph.VerticeList[i].AF))
            file.write('\n')
            file.write('\n')
        file.write('\n')

    #General Infos (bottom of output file)
    file.write('INFO')
    file.write('\n')
    file.write('====')
    file.write('\n')
    file.write('\n')
    file.write('Generate Graph Input Parameters:')
    file.write('\n')
    file.write('    Max_color_Generate_Graph: ' + str(m))
    file.write('\n')
    file.write('    degree: ' + str(d))
    file.write('\n')
    file.write('\n')
    file.write('Generated Graph Info:')
    file.write('\n')
    file.write('    number_balls: ' + str(len(NHGraph.VerticeList)))
    file.write('\n')
    file.write('    number total_adjacents: ' + str(NHGraph.TotAdj /2))
    file.write('\n')
    file.write('    Laufzeit GenerateGraph: ' + str(NHGraph.LaufzeitGenerateGraph))
    file.write('\n')
    file.write('\n')
    file.write('Ausgabefaerbung SATSolver Info:')
    file.write('\n')
    file.write('    Max_color_Faerbung_input: ' + str(ma))
    file.write('\n')
    file.write('    Max_color_Faerbung_output: ' + str(NHGraph.MaxColorOutput))
    file.write('\n')
    file.write('    Number_of_CNF_clauses: ' + str(NHGraph.NOC))
    file.write('\n')
    file.write('    SAT: ' + str(NHGraph.SAT))
    file.write('\n')
    file.write('    Solution: ' + str(NHGraph.Solution))
    file.write('\n')
    file.write('    Problem: ' + str(NHGraph.Problem))
    file.write('\n')
    file.write('    Laufzeit Ausgabefaerbung: ' + str(NHGraph.LaufzeitAusgabefärbung))
    file.write('\n')
    file.write('\n')
    file.write('Other Infos:')
    file.write('\n')
    file.write('    Valid: ' + str(NHGraph.Valid))

    #terminal print
    """
    for i in range(len(NHGraph.VerticeList)):
        print("mc: " + str(NHGraph.VerticeList[i].Ball.MyLocalView.MyColor) + "\n nc: ", end = '')
        for j in range(len(NHGraph.VerticeList[i].Ball.MyLocalView.NeighborColors)):
            print(str(NHGraph.VerticeList[i].Ball.MyLocalView.NeighborColors[j]) + " ", end = '')
        print("")

        # to turn off adjacent balls, comment below
        
        for k in range(len(NHGraph.VerticeList[i].Ball.MyLocalView.can_be_adjacent)):
            current_adjacent_view = NHGraph.VerticeList[i].Ball.MyLocalView.can_be_adjacent[k].MyLocalView
            print(" cba mc: " + str(current_adjacent_view.MyColor) + " nc: ", end = '')
            for j in range(len(current_adjacent_view.NeighborColors)):
                print(str(current_adjacent_view.NeighborColors[j]) + " ", end = '')
            print("")
        print("")
    """


# enum, currently not in use
class Strategy(Enum):
    Distribute_Colors = 0
