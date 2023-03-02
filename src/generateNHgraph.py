#This file generates the neighborhood graph with a valid vertex coloring

import copy
from src.dataclassesGraph import *
import time

def generate_NHGraph(max_color: int, max_degree: int, NH_graph: list):
    
    print("start generating Graph...")

    st = time.process_time()

    #generate for every ball a nc list
    for degree in range(1, max_degree+1):
        for mc in range(1,max_color+1):
            temp_nc_lst = []

            #fill the nc list with start values (-1)
            for i in range(degree):
                temp_nc_lst.append(-1)
            current_degree = [-1] #has to be object, becaus pass by reference
            
            #rekursiveley add the right nc to nc list
            rek_nc_add_v2(temp_nc_lst, max_color, degree, current_degree, NH_graph, mc)

    assign_position_in_vertexList(NH_graph)

    generate_adjacents(NH_graph)

    color_vertexs(NH_graph)

    et = time.process_time()
    NH_graph.LaufzeitGenerateGraph = (et - st)

    print("generating Graph finished \n")

    #print(str(NH_graph.LaufzeitGenerateGraph))

    return 0

def rek_nc_add(temp_nc_lst, max_color, degree, current_degree, NH_graph, mc):

    current_degree[0] += 1
    start = 1

    #start at the right color
    if(current_degree[0] != 0):
        start = temp_nc_lst[current_degree[0]-1]

    #iterate through every possible color
    for color in range(start,max_color+1):

        skip = 0

        #we found a valid nc color
        if(color != mc):
            temp_nc_lst[current_degree[0]] = color
        else:
            skip = 1

        if(not skip):
            #nc list is complete and ball with vertex can be generated
            if (current_degree[0] == (degree-1)):
                vertex_ = vertexC()
                vertex_.Ball = BallC()
                vertex_.Ball.MyLocalView = LocalViewC()
                vertex_.Ball.MyLocalView.NeighborColors = []
                vertex_.Ball.Adjacents = []
                vertex_.Ball.MyLocalView.MyColor = mc

                for i in range(len(temp_nc_lst)):
                    vertex_.Ball.MyLocalView.NeighborColors.append(temp_nc_lst[i])
    
                NH_graph.vertexList.append(vertex_)

            #nc list is not yet complete
            else:
                rek_nc_add(temp_nc_lst, max_color, degree, current_degree, NH_graph, mc)

        #we reached the maximum possible color
        if (color == max_color):
            current_degree[0] -= 1
            break
        
    NH_graph.Valid = True


#a second version, generating balls with no duplicate nc
def rek_nc_add_v2(temp_nc_lst, max_color, degree, current_degree, NH_graph, mc):

    current_degree[0] += 1
    start = 1

    #start at the right color
    if(current_degree[0] != 0):
        start = temp_nc_lst[current_degree[0]-1]

    #iterate through every possible color
    for color in range(start,max_color+1):

        duplicate_flag = False
        skip = 0

        #we found a valid nc color
        if(color != mc):
            #check for duplicate colors
            if(temp_nc_lst[current_degree[0]-1] == color):
                duplicate_flag = True
            else:    
                temp_nc_lst[current_degree[0]] = color
        else:
            skip = 1

        if(not skip):
            #we have duplicate nc colors, so we dont generate that node
            if(duplicate_flag):
                continue

            #nc list is complete and ball with vertex can be generated
            elif (current_degree[0] == (degree-1)):
                vertex_ = vertexC()
                vertex_.Ball = BallC()
                vertex_.Ball.MyLocalView = LocalViewC()
                vertex_.Ball.MyLocalView.NeighborColors = []
                vertex_.Ball.Adjacents = []
                vertex_.Ball.MyLocalView.MyColor = mc

                for i in range(len(temp_nc_lst)):
                    vertex_.Ball.MyLocalView.NeighborColors.append(temp_nc_lst[i])
    
                NH_graph.vertexList.append(vertex_)

            #nc list is not yet complete
            else:
                rek_nc_add_v2(temp_nc_lst, max_color, degree, current_degree, NH_graph, mc)

        #we reached the maximum possible color
        if (color == max_color):
            current_degree[0] -= 1
            break
        
    NH_graph.Valid = True
        
#Sets Position in vertexList, which we need for clororing with SAT-Solver
def assign_position_in_vertexList(NHGraph):
    for vertex in range(len(NHGraph.vertexList)):
        NHGraph.vertexList[vertex].PositionInvertexList = vertex


#Fills the Adjacents List
def generate_adjacents(NHGraph):
    for vertex in range(len(NHGraph.vertexList)):
        current_ball = NHGraph.vertexList[vertex].Ball

        #now compare every other ball to this ball
        for nb in range(len(NHGraph.vertexList)):
            comparison(NHGraph, current_ball, nb)
            
#this checks if (my ball)mc is in (other ball)nc, and (my ball)nc is in (other ball)mc
def comparison(NHGraph, current_ball, nb):
    for nc in range(len(NHGraph.vertexList[nb].Ball.MyLocalView.NeighborColors)):

        if(current_ball.MyLocalView.MyColor == NHGraph.vertexList[nb].Ball.MyLocalView.NeighborColors[nc]):
            for mnc in range(len(current_ball.MyLocalView.NeighborColors)):

                if(current_ball.MyLocalView.NeighborColors[mnc] == NHGraph.vertexList[nb].Ball.MyLocalView.MyColor):
                    current_ball.Adjacents.append(copy.copy(NHGraph.vertexList[nb]))
                    NHGraph.TotAdj += 1
                    return


#Single Function to check, if 2 Balls are adjacent
'''
def can_be_adjacent(Ball1, Ball2):
    for nc2 in range(len(Ball2.NeighborColors)):
        if (Ball1.MyLocalView.MyColor == Ball2.NeighborColors[nc2]):
            
            for nc1 in range(len(Ball1.NeighborColors)):
                if (Ball2.MyLocalView.MyColor == Ball1.NeighborColors[nc1]):
                    return 1
    return 0
'''

#Set initial color of the vertex to MyColor of the Ball
def color_vertexs(NHGraph):
    for vertex in range(len(NHGraph.vertexList)):
        NHGraph.vertexList[vertex].AF = NHGraph.vertexList[vertex].Ball.MyLocalView.MyColor
