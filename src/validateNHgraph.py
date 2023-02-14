from src.dataclasses_graph import *

def validation(NHGraph):

    NHGraph.MaxColorOutput = 0
    for vertice in range(len(NHGraph.VerticeList)):
        for adjacent in range(len(NHGraph.VerticeList[vertice].Ball.Adjacents)):

            if(NHGraph.VerticeList[vertice].AF > NHGraph.MaxColorOutput):
                NHGraph.MaxColorOutput = NHGraph.VerticeList[vertice].AF

            if(NHGraph.VerticeList[vertice].AF == NHGraph.VerticeList[vertice].Ball.Adjacents[adjacent].AF):
                NHGraph.Valid = False

    return 0