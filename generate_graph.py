
import networkx
import numpy
import matplotlib.pyplot as plt


def generateNeighborhoodGraph(rounds: int, max_colour: int, max_degree: int):
    #print("generateNeighborhoodGraph\n rounds:" + str(rounds) +"\n max_colour:"+ str(max_colour)+"\n max_edges:"+ str(max_degree))
    
    if (max_degree >= max_colour):
        print("invalid input for generating valid Neighbourhoodgraph\n (Check max degree and number of colors input)")
        return 1


    all_graphs_list = []

    #fill graphs list with categories by degrees
    for degree in range(max_degree+1):
        degree_graphs_list = []
        all_graphs_list.append(degree_graphs_list)

        #generate the graphs
        for color in range(max_colour * 2):
            network = networkx.Graph()

            #add the nodes to the graph
            for node in range(degree+1):
                network.add_node(node)

            #add edges between the nodes
            for edge in range(degree):
                network.add_edge(0,edge+1)

            #add final graph    
            all_graphs_list[degree].append(network)
            
    #print graph(s)
    print_network = all_graphs_list[2][2]
    networkx.draw_networkx(print_network)

    ax = plt.gca()
    ax.margins(0.10)
    plt.axis("off")
    plt.show()

    return 0