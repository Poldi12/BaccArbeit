
import networkx
import helpers
import color_networkx

def generateNeighborhoodGraph(rounds: int, max_colour: int, degree: int, all_balls_list: list):
    #print("generateNeighborhoodGraph\n rounds:" + str(rounds) +"\n max_colour:"+ str(max_colour)+"\n max_edges:"+ str(max_degree))

    # selects, how to generate and first color the graphs
    match helpers.Strategy:

        case Distribute_Colors:
            #amount of balls
            for i in range(degree+1): #amount of possible color patterns

                network = networkx.Graph()

                #add the nodes to the ball
                for node in range(degree+1):
                    network.add_node(node)

                #add edges between the nodes
                for edge in range(degree):
                    network.add_edge(0,edge+1)

                #eingabefaerbung ball
                #color_networkx.eingabefaerbung()

                #add final graph    
                all_balls_list.append(network)

    helpers.print_ball_(all_balls_list, 0)

    return 0