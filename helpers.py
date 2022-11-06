import networkx
import matplotlib.pyplot as plt

#print selected graph (maybe more fuctionality in the future)
def print_ball_(all_balls_list, position):

    print_ball = all_balls_list[position]
    networkx.draw_networkx(print_ball, with_labels=True)

    ax = plt.gca()
    ax.margins(0.10)
    plt.axis("on")
    plt.show()