#This file contains the print functionalities (terminal, output file)

from src.dataclassesGraph import *
import os

def print_NHGraph(NHGraph, m , d, ma, file_name, used_solver):

    #only print to output file if a path is provided
    if(file_name != 'nooutputprovided!.txt'):

        file = open(file_name, 'w')
    
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
        file.write('    number_balls: ' + str(len(NHGraph.vertexList)))
        file.write('\n')
        file.write('    number total_adjacents: ' + str(NHGraph.TotAdj /2))
        file.write('\n')
        file.write('    Laufzeit GenerateGraph: ' + str(NHGraph.LaufzeitGenerateGraph))
        file.write('\n')
        file.write('\n')
        file.write('Ausgabefaerbung SATSolver Info:')
        file.write('\n')
        file.write('    Solver: ' + used_solver)
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
        file.write('    Laufzeit Ausgabefaerbung: ' + str(NHGraph.LaufzeitAusgabefärbung))
        file.write('\n')
        file.write('\n')
        file.write('Other Infos:')
        file.write('\n')
        file.write('    Valid: ' + str(NHGraph.Valid))
        file.write('\n')
        
        file.close()
        
        #change file permissions to "everyone read, write, execute"
        os.chmod(file_name, 0o777)

    #General Infos in terminal (bottom of output file)
    print('')
    print('INFO')
    print('====')
    print('Ausgabefaerbung SATSolver Info:')
    print('    Solver: ' + used_solver)
    print('    Max_color_Faerbung_input: ' + str(ma))
    print('    Max_color_Faerbung_output: ' + str(NHGraph.MaxColorOutput))
    print('    Number_of_CNF_clauses: ' + str(NHGraph.NOC))
    print('    SAT: ' + str(NHGraph.SAT))
    print('    Solution: ' + str(NHGraph.Solution))
    print('    Laufzeit Ausgabefaerbung: ' + str(NHGraph.LaufzeitAusgabefärbung))
    print('Other Infos:')
    print('    Valid: ' + str(NHGraph.Valid))
    
#print networkx could be used to visualise graph, not implemented!

#import networkx
#import matplotlib.pyplot as plt

'''
def print_networkx(all_balls_list, position):

    print_ball = all_balls_list[position]
    networkx.draw_networkx(print_ball, with_labels=True)

    ax = plt.gca()
    ax.margins(0.10)
    plt.axis("on")
    plt.show()
'''

def print_graph_infos(NHGraph, m , d):
    print('INFO')
    print('====')
    print('Generate Graph Input Parameters:')
    print('    Max_color_Generate_Graph: ' + str(m))
    print('    degree: ' + str(d))
    print('Generated Graph Info:')
    print('    number_balls: ' + str(len(NHGraph.vertexList)))
    print('    number total_adjacents: ' + str(NHGraph.TotAdj /2))
    print('    Laufzeit GenerateGraph: ' + str(NHGraph.LaufzeitGenerateGraph))
    print()

    return 0

#prints whole nh graph to file
def print_whole_graph(NHGraph, filename):

    file = open(filename+'-Graph', 'w')

    file.write('Neighborhood Graph with initial coloring:')
    file.write('\n')
    file.write('\n')
    for i in range(len(NHGraph.vertexList)):
        # ball with mc and ncs
        file.write('mc: ' + str(NHGraph.vertexList[i].Ball.MyLocalView.MyColor) + '\n nc: ')
        for j in range(len(NHGraph.vertexList[i].Ball.MyLocalView.NeighborColors)):
            file.write(str(NHGraph.vertexList[i].Ball.MyLocalView.NeighborColors[j]) + ' ')
        file.write('\n')
        # possible adjacents 
        for k in range(len(NHGraph.vertexList[i].Ball.Adjacents)):
            current_adjacent_view = NHGraph.vertexList[i].Ball.Adjacents[k].Ball.MyLocalView
            file.write(' cba mc: ' + str(current_adjacent_view.MyColor) + ' nc: ')
            for j in range(len(current_adjacent_view.NeighborColors)):
                file.write(str(current_adjacent_view.NeighborColors[j]) + ' ')
            file.write('\n')
        file.write('number_adjacents:' + str(len(NHGraph.vertexList[i].Ball.Adjacents)))
        file.write('\n')
        # vertexs
        file.write('vertex_ausgabefaerbung:' + str(NHGraph.vertexList[i].AF))
        file.write('\n')
        file.write('\n')

    return 0