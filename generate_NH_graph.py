
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

    #generate all neighbors with my_color
    for mc in range(max_color):

        for degree_ in range(degree):
            used_lst = []
            for nc_add in range(max_color):
                
                # search for duplicates in list
                i = 0
                do_not_set = 0
                while (i < len(temp_nc_lst)):
                    if(temp_nc_lst[i] == nc_add):
                        do_not_set = 1
                        break
                    i += 1

                if(not do_not_set):
                    #if last neighbor is reached, add ball and stop
                    if(degree_ == (degree -1)):
                        temp_nc_lst.append(nc_add)

                        ball_ = Ball()
                        ball_.mylocalview = LocalView()
                        ball_.mylocalview.neighbor_colors = []

                        ball_.mylocalview.my_color = mc
                        ball_.mylocalview.neighbor_colors = temp_nc_lst
                        temp_nc_lst = []
                        NH_graph.SetOfBall.append(ball_)
                        break
                    #still more neighbors to add
                    temp_nc_lst.append(nc_add)
                    break

                current_nc += 1
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

