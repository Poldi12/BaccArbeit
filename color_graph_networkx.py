import networkx
import helpers

def eingabefaerbung(all_balls_list):
    
    #color all graphs in all_graphs_list
    for degree in range(len(all_balls_list)):
        for color in range(len(all_balls_list[degree])):

            networkx.coloring.greedy_color(all_balls_list[degree][color], strategy="largest_first")

    helpers.print_ball_(all_balls_list, 1)

    return 0

def ausgabefaerbung(all_balls_list):

    return 0