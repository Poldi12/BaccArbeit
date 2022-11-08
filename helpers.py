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

# enum, currently not in use
class Strategy(Enum):
    Distribute_Colors = 0


    

