
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

    NHGraph_ = NHGraph()

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
                if((len(NHGraph_.SetOfBall) >= 1) and (NHGraph_.SetOfBall[len(NHGraph_.SetOfBall)-1].mylocalview.neighbor_colors[0] == neighbors + neighbor_offset)):
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
            

            NHGraph_.SetOfBall.append(ball_)

    print_NHGraph(NHGraph_)
    return 0

def print_NHGraph(NHGraph: NHGraph):
    for i in range(len(NHGraph.SetOfBall)):
        print("mc: " + str(NHGraph.SetOfBall[i].mylocalview.my_color) + "\n nc: ", end = '')
        for j in range(len(NHGraph.SetOfBall[i].mylocalview.neighbor_colors)):
            print(str(NHGraph.SetOfBall[i].mylocalview.neighbor_colors[j]) + " ", end = '')
        print("")