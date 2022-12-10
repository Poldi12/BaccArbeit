import helpers
from generateNHgraph import *

#NOT working!

#look at neighbors, reduce mc to smallest possible color
def af_first(NH_graph, max_color):

    NH_graph = NHGraph

    for ball in range(len(NH_graph.VerticeList)):
        possible_color = -1
        skip = 0

        for color in range(max_color):
            current_mc = NH_graph.VerticeList[ball].Ball.mylocalview.my_color
            if(color != current_mc):
                
                for nc in range(len(NH_graph.VerticeList[ball].Ball.mylocalview.neighbor_colors)):
                    current_nc = NH_graph.VerticeList[ball].Ball.mylocalview.neighbor_colors[nc]

                    if((not skip) and (color < current_nc)):
                        possible_color = color
                        skip = 1
                    if(possible_color >= current_nc):
                        possible_color = -1
                        skip = 0

        if(possible_color != -1):
            NH_graph.VerticeList[ball].Ball.mylocalview.my_color = possible_color

    #helpers.print_NHGraph(NH_graph)

    return 0