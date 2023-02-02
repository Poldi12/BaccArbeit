import copy
from dataclasses_graph import *
import time

def generate_NHGraph(max_color: int, max_degree: int, NH_graph: list):
    #print("generateNeighborhoodGraph\n rounds:" + str(rounds) +"\n max_colour:"+ str(max_colour)+"\n max_edges:"+ str(max_degree))

    print("start generating Graph...")

    st = time.process_time()

    #generate NH_graph rekursive with "Eingabefaerbung"
    for degree in range(1, max_degree+1):

        for mc in range(1,max_color+1):

            temp_nc_lst = []
            for i in range(degree):
                temp_nc_lst.append(-1)
            current_degree = [-1]
            
            rek_nc_add(temp_nc_lst, max_color, degree, current_degree, NH_graph, mc)

    assign_position_in_VerticeList(NH_graph)

    generate_adjacents(NH_graph)

    color_vertices(NH_graph)

    et = time.process_time()
    
    NH_graph.LaufzeitGenerateGraph = (et - st)

    print("generating Graph finished \n")

    #print(str(NH_graph.LaufzeitGenerateGraph))

    return 0

def rek_nc_add(temp_nc_lst, max_color, degree, current_degree, NH_graph, mc):
    current_degree[0] += 1
    start = 1
    if(current_degree[0] != 0):
        start = temp_nc_lst[current_degree[0]-1]

    for color in range(start,max_color+1):

        skip = 0
        if(color != mc):
            temp_nc_lst[current_degree[0]] = color
        else:
            skip = 1

        if(not skip):
            if (current_degree[0] == (degree-1)):
                vertice_ = VerticeC()
                vertice_.Ball = BallC()
                vertice_.Ball.MyLocalView = LocalViewC()
                vertice_.Ball.MyLocalView.NeighborColors = []
                vertice_.Ball.Adjacents = []
                vertice_.Ball.MyLocalView.MyColor = mc

                for i in range(len(temp_nc_lst)):
                    vertice_.Ball.MyLocalView.NeighborColors.append(temp_nc_lst[i])
    
                NH_graph.VerticeList.append(vertice_)

            else:
                rek_nc_add(temp_nc_lst, max_color, degree, current_degree, NH_graph, mc)

        if (color == max_color):
            current_degree[0] -= 1
            break
        
    NH_graph.Valid = True
        
#Sets Position in VerticeList, which we need for clororing with SAT-Solver
def assign_position_in_VerticeList(NHGraph):
    for vertice in range(len(NHGraph.VerticeList)):
        NHGraph.VerticeList[vertice].PositionInVerticeList = vertice


#Fills the Adjacents List
def generate_adjacents(NHGraph):
    for vertice in range(len(NHGraph.VerticeList)):
        current_ball = NHGraph.VerticeList[vertice].Ball

        # now compare every other ball to this ball
        for nb in range(len(NHGraph.VerticeList)):
            comparison(NHGraph, current_ball, nb)
            
def comparison(NHGraph, current_ball, nb):
    for nc in range(len(NHGraph.VerticeList[nb].Ball.MyLocalView.NeighborColors)):

        if(current_ball.MyLocalView.MyColor == NHGraph.VerticeList[nb].Ball.MyLocalView.NeighborColors[nc]):
            for mnc in range(len(current_ball.MyLocalView.NeighborColors)):

                if(current_ball.MyLocalView.NeighborColors[mnc] == NHGraph.VerticeList[nb].Ball.MyLocalView.MyColor):
                    current_ball.Adjacents.append(copy.copy(NHGraph.VerticeList[nb]))
                    NHGraph.TotAdj += 1
                    return


#Single Function to check, if 2 Balls are adjacent
def can_be_adjacent(Ball1, Ball2):
    for nc2 in range(len(Ball2.NeighborColors)):
        if (Ball1.MyLocalView.MyColor == Ball2.NeighborColors[nc2]):
            
            for nc1 in range(len(Ball1.NeighborColors)):
                if (Ball2.MyLocalView.MyColor == Ball1.NeighborColors[nc1]):
                    return 1
    return 0


#Set initial color of the Vertice AF
def color_vertices(NHGraph):
    for vertice in range(len(NHGraph.VerticeList)):
        NHGraph.VerticeList[vertice].AF = NHGraph.VerticeList[vertice].Ball.MyLocalView.MyColor
