
import networkx
import helpers
import color_graph_networkx

def generateNeighborhoodGraph(rounds: int, max_colour: int, degree: int, all_balls_list: list):
    #print("generateNeighborhoodGraph\n rounds:" + str(rounds) +"\n max_colour:"+ str(max_colour)+"\n max_edges:"+ str(max_degree))

    #fill list with graphs of all legit coloring patterns for neighborhood graphs
    for i in range(degree+1): #amount of possible color patterns

            network = networkx.Graph()

            #add the nodes to the graph
            for node in range(degree+1):
                network.add_node(node)

            #add edges between the nodes
            for edge in range(degree):
                network.add_edge(0,edge+1)

            #color graph
            #color_graph_networkx.eingabefaerbung()

            #add final graph    
            all_balls_list.append(network)

    helpers.print_ball_(all_balls_list, 0)

    return 0