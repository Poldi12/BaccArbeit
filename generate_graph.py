
import networkx
import numpy
import matplotlib.pyplot as plt


def generateNeighborhoodGraph(rounds: int, max_colour: int, max_degree: int, all_graphs_list: list):
    #print("generateNeighborhoodGraph\n rounds:" + str(rounds) +"\n max_colour:"+ str(max_colour)+"\n max_edges:"+ str(max_degree))

    #fill graphs list with degree categories lists
    for degree in range(max_degree+1):
        degree_graphs_list = []
        all_graphs_list.append(degree_graphs_list)

        #generate the graphs (determine how much graphs we need for given degree and max color)
        for color in range(max_colour * 2):
            network = networkx.Graph()

            #add the nodes to the graph
            for node in range(degree+1):
                network.add_node(node)

            #add edges between the nodes
            for edge in range(degree):
                network.add_edge(0,edge+1)

            #color graph


            #add final graph    
            all_graphs_list[degree].append(network)

    print_graph(all_graphs_list, 2,2)

    return 0

#print selected graph (maybe more fuctionality in the future)
def print_graph(all_graphs_list, degree, coloring):

    print_network = all_graphs_list[degree][coloring]
    networkx.draw_networkx(print_network, with_labels=True)

    ax = plt.gca()
    ax.margins(0.10)
    plt.axis("on")
    plt.show()