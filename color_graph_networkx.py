import networkx
import generate_graph

def colorGraph(all_graphs_list):
    
    #color all graphs in all_graphs_list
    for degree in range(len(all_graphs_list)):
        for color in range(len(all_graphs_list[degree])):

            networkx.coloring.greedy_color(all_graphs_list[degree][color], strategy="largest_first")

    generate_graph.print_graph(all_graphs_list, 2, 2)

    return 0