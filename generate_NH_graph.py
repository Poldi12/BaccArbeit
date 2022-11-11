
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

    NHGraph_ = NHGraph

    #generate balls
    for color in range(max_color):

        ball_ = Ball()
        ball_.mylocalview = LocalView()

        ball_.mylocalview.my_color = color

        #set neighbor colors
        for neighbors in range(degree):
            if(((neighbors) != color) and ((neighbors) <= max_color)):
                ball_.mylocalview.neighbor_colors.append(neighbors)

        NHGraph_.SetOfBall.append(ball_)

    print_NHGraph(NHGraph_)
    return 0

def print_NHGraph(NHGraph: NHGraph):
    for i in range(len(NHGraph.SetOfBall)):
        print(str(NHGraph.SetOfBall[i].mylocalview.my_color))
        for j in range(len(NHGraph.SetOfBall[i].mylocalview.neighbor_colors)):
            print(str(NHGraph.SetOfBall[i].mylocalview.neighbor_colors[j]) + " ", end = '')
        print("")