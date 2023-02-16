#This file contains validation of the vertex colorings and finding of the current max color in the graph

from src.dataclassesGraph import *

def validation(NHGraph):

    NHGraph.MaxColorOutput = 0
    for vertice in range(len(NHGraph.VerticeList)):
        for adjacent in range(len(NHGraph.VerticeList[vertice].Ball.Adjacents)):

            #find max color in graph
            if(NHGraph.VerticeList[vertice].AF > NHGraph.MaxColorOutput):
                NHGraph.MaxColorOutput = NHGraph.VerticeList[vertice].AF

            #check vertex coloring for correctness
            if(NHGraph.VerticeList[vertice].AF == NHGraph.VerticeList[vertice].Ball.Adjacents[adjacent].AF):
                NHGraph.Valid = False

    return 0