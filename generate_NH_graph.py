
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

    temp_nc_lst = []
    for i in range(degree):
        temp_nc_lst.append(-1)

    current_degree = [-1]

    #generate NH_graph rekursive
    for mc in range(max_color+1):

        rek_nc_add(temp_nc_lst, max_color, degree, current_degree, NH_graph, mc)
        
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
    start = 0
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
                ball_ = Ball()
                ball_.mylocalview = LocalView()
                ball_.mylocalview.neighbor_colors = []

                ball_.mylocalview.my_color = mc
                for i in range(len(temp_nc_lst)):
                    ball_.mylocalview.neighbor_colors.append(temp_nc_lst[i])
    
                NH_graph.SetOfBall.append(ball_)

            else:
                rek_nc_add(temp_nc_lst, max_color, degree, current_degree, NH_graph, mc)

        if (color == max_color):
            current_degree[0] -= 1
            break
        