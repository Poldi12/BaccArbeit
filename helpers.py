import networkx
import matplotlib.pyplot as plt
from enum import Enum

#print networkx, currently not in use
def print_networkx(all_balls_list, position):

    print_ball = all_balls_list[position]
    networkx.draw_networkx(print_ball, with_labels=True)

    ax = plt.gca()
    ax.margins(0.10)
    plt.axis("on")
    plt.show()

def print_NHGraph(NHGraph):

    file = open('output.txt', 'w')

    for i in range(len(NHGraph.SetOfBall)):
        file.write('mc: ' + str(NHGraph.SetOfBall[i].mylocalview.my_color) + '\n nc: ')
        for j in range(len(NHGraph.SetOfBall[i].mylocalview.neighbor_colors)):
            file.write(str(NHGraph.SetOfBall[i].mylocalview.neighbor_colors[j]) + ' ')
        file.write('\n')

        # to turn off adjacent balls, comment below
        
        for k in range(len(NHGraph.SetOfBall[i].mylocalview.can_be_adjacent)):
            current_adjacent_view = NHGraph.SetOfBall[i].mylocalview.can_be_adjacent[k].mylocalview
            file.write(' cba mc: ' + str(current_adjacent_view.my_color) + ' nc: ')
            for j in range(len(current_adjacent_view.neighbor_colors)):
                file.write(str(current_adjacent_view.neighbor_colors[j]) + ' ')
            file.write('\n')
        file.write('\n')

    #terminal print
    """
    for i in range(len(NHGraph.SetOfBall)):
        print("mc: " + str(NHGraph.SetOfBall[i].mylocalview.my_color) + "\n nc: ", end = '')
        for j in range(len(NHGraph.SetOfBall[i].mylocalview.neighbor_colors)):
            print(str(NHGraph.SetOfBall[i].mylocalview.neighbor_colors[j]) + " ", end = '')
        print("")

        # to turn off adjacent balls, comment below
        
        for k in range(len(NHGraph.SetOfBall[i].mylocalview.can_be_adjacent)):
            current_adjacent_view = NHGraph.SetOfBall[i].mylocalview.can_be_adjacent[k].mylocalview
            print(" cba mc: " + str(current_adjacent_view.my_color) + " nc: ", end = '')
            for j in range(len(current_adjacent_view.neighbor_colors)):
                print(str(current_adjacent_view.neighbor_colors[j]) + " ", end = '')
            print("")
        print("")
    """


# enum, currently not in use
class Strategy(Enum):
    Distribute_Colors = 0
