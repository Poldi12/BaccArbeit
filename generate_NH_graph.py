
import networkx
import helpers
import color_networkx
from dataclasses import dataclass

@dataclass
class LocalView:
    my_color: int = None
    neighbor_colors = []
    can_be_adjacent: bool = None

@dataclass
class Ball:
    mylocalview: LocalView = None

@dataclass
class NHGraph:
    SetOfBall = []

def generateNeighborhoodGraph(rounds: int, max_color: int, degree: int, NH_graph: list):
    #print("generateNeighborhoodGraph\n rounds:" + str(rounds) +"\n max_colour:"+ str(max_colour)+"\n max_edges:"+ str(max_degree))

    NH_graph = NHGraph()

    #generate dic with my_color values and neighbor_color values
    """
    mc_dict = dict()
    nc_dict = dict()

    for i in range(max_color):
        mc_dict.update({i,0})
    for i in range(max_color):
        nc_dict.update({i,0})
    """
    
    temp_nc_lst = []
    for i in range(degree):
        temp_nc_lst.append(-1)

    current_degree = [-1]

    #generate all neighbors with my_color
    for mc in range(max_color):

        rek_nc_add(temp_nc_lst, max_color, degree, current_degree, NH_graph, mc)
        
    """            
    # now delete nc if nc == mc
    for i in range(len(NH_graph.SetOfBall)):
        for j in range(len(NH_graph.SetOfBall[i].mylocalview.neighbor_colors)):
            if(NH_graph.SetOfBall[i].mylocalview.neighbor_colors[j] == NH_graph.SetOfBall[i].mylocalview.my_color):
                NH_graph.SetOfBall[i].mylocalview.neighbor_colors.remove(NH_graph.SetOfBall[i].mylocalview.my_color)
                j -= 1
    """

                


        
    """
    #generate balls
    for color in range(max_color):
        first = 0
        for neighbor_offset in range(max_color + 1 - degree):

            ball_ = Ball()
            ball_.mylocalview = LocalView()
            ball_.mylocalview.neighbor_colors = []

            ball_.mylocalview.my_color = color

            equal_offset = 0
            neighbors = 0
            
            #set neighbor colors
            while (neighbors < (degree + equal_offset)):
                if((len(NH_graph.SetOfBall) >= 1) and (NH_graph.SetOfBall[len(NH_graph.SetOfBall)-1].mylocalview.neighbor_colors[0] == neighbors + neighbor_offset)):
                    first = 1
                if((neighbors + neighbor_offset) == color):
                    equal_offset = 1

                if(((neighbors + neighbor_offset) != color) and ((neighbors + neighbor_offset) <= max_color)):
                    if((neighbors + neighbor_offset + first) == max_color):
                        ball_.mylocalview.neighbor_colors.append(0)
                    else:
                        ball_.mylocalview.neighbor_colors.append(neighbors + neighbor_offset + first)

                neighbors += 1
                #if mylocalview is in neighbors list, we need one more node
            

            NH_graph.SetOfBall.append(ball_)
"""
    print_NHGraph(NH_graph)
    return 0

def print_NHGraph(NHGraph: NHGraph):
    for i in range(len(NHGraph.SetOfBall)):
        print("mc: " + str(NHGraph.SetOfBall[i].mylocalview.my_color) + "\n nc: ", end = '')
        for j in range(len(NHGraph.SetOfBall[i].mylocalview.neighbor_colors)):
            print(str(NHGraph.SetOfBall[i].mylocalview.neighbor_colors[j]) + " ", end = '')
        print("")

def rek_nc_add(temp_nc_lst, max_color, degree, current_degree, NH_graph, mc):
    current_degree[0] += 1
    for color in range(max_color+1):
        temp_nc_lst[current_degree[0]] = color
        if (current_degree[0] == (degree-1)):
            ball_ = Ball()
            ball_.mylocalview = LocalView()
            ball_.mylocalview.neighbor_colors = []

            ball_.mylocalview.my_color = mc
            ball_.mylocalview.neighbor_colors = temp_nc_lst
            NH_graph.SetOfBall.append(ball_)
        else:
            rek_nc_add(temp_nc_lst, max_color, degree, current_degree, NH_graph, mc)
        if (color == max_color):
            current_degree[0] -= 1
            break
        
