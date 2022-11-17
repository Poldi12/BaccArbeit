import helpers
from dataclasses import dataclass
import copy

@dataclass
class LocalView:
    my_color: int = None
    neighbor_colors = []
    can_be_adjacent = []

@dataclass
class Ball:
    mylocalview: LocalView = None

@dataclass
class NHGraph:
    SetOfBall = []

def generateNeighborhoodGraph(rounds: int, max_color: int, max_degree: int, NH_graph: list):
    #print("generateNeighborhoodGraph\n rounds:" + str(rounds) +"\n max_colour:"+ str(max_colour)+"\n max_edges:"+ str(max_degree))

    NH_graph = NHGraph()

    #generate NH_graph rekursive with "Eingabefaerbung"
    for degree in range(1, max_degree+1):

        for mc in range(max_color+1):

            temp_nc_lst = []
            for i in range(degree):
                temp_nc_lst.append(-1)
            current_degree = [-1]
            
            rek_nc_add(temp_nc_lst, max_color, degree, current_degree, NH_graph, mc)
        
    can_be_adjacent(NHGraph)

    #helpers.print_NHGraph(NH_graph)
    return 0

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
                ball_.mylocalview.can_be_adjacent = []

                ball_.mylocalview.my_color = mc
                for i in range(len(temp_nc_lst)):
                    ball_.mylocalview.neighbor_colors.append(temp_nc_lst[i])
    
                NH_graph.SetOfBall.append(ball_)

            else:
                rek_nc_add(temp_nc_lst, max_color, degree, current_degree, NH_graph, mc)

        if (color == max_color):
            current_degree[0] -= 1
            break
        
def can_be_adjacent(NHGraph):
    for ball in range(len(NHGraph.SetOfBall)):
        current_view = NHGraph.SetOfBall[ball].mylocalview

        #if((ball+1) != len(NHGraph.SetOfBall)): ball+1, only combine first found
        for nb in range(len(NHGraph.SetOfBall)):
            for nc in range(len(NHGraph.SetOfBall[nb].mylocalview.neighbor_colors)):

                break_again = 0
                if(current_view.my_color == NHGraph.SetOfBall[nb].mylocalview.neighbor_colors[nc]):
                    for mnc in range(len(current_view.neighbor_colors)):

                        if(current_view.neighbor_colors[mnc] == NHGraph.SetOfBall[nb].mylocalview.my_color):

                            current_view.can_be_adjacent.append(copy.deepcopy(NHGraph.SetOfBall[nb]))
                            break_again = 1
                            break

                if(break_again):
                        break
