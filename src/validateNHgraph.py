#This file contains validation of the vertex colorings and finding of the current max color in the graph

from src.dataclassesGraph import *

def validation(NHGraph):

    NHGraph.MaxColorOutput = 0
    for vertex in range(len(NHGraph.vertexList)):
        for adjacent in range(len(NHGraph.vertexList[vertex].Ball.Adjacents)):

            #find max color in graph
            if(NHGraph.vertexList[vertex].AF > NHGraph.MaxColorOutput):
                NHGraph.MaxColorOutput = NHGraph.vertexList[vertex].AF

            #check vertex coloring for correctness
            if(NHGraph.vertexList[vertex].AF == NHGraph.vertexList[vertex].Ball.Adjacents[adjacent].AF):
                NHGraph.Valid = False

    return 0