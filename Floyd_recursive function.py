# We define a very large number to represent that there is no path between two nodes
import sys
import itertools

NO_PATH = sys.maxsize

# This is our graph represented as a 2D list (matrix)
graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]

# The length of our graph (number of nodes)
num_nodes = len(graph[0])

def find_shortest_path(graph, start_node, end_node, intermediate):
    # If there are no more intermediate nodes to consider, return the direct path
    if intermediate == 0:
        return graph[start_node][end_node]

    # Find the shortest path without the intermediate node
    shortest_without_intermediate = find_shortest_path(graph, start_node, end_node, intermediate - 1)
    
    # Find the shortest path with the intermediate node
    shortest_with_intermediate = (find_shortest_path(graph, start_node, intermediate - 1, intermediate - 1) +
                                  find_shortest_path(graph, intermediate - 1, end_node, intermediate - 1))

    # Return the shorter of the two paths
    return min(shortest_without_intermediate, shortest_with_intermediate)

# For each pair of nodes, we find and print the shortest path
for start_node in range(num_nodes):
    for end_node in range(num_nodes):
        shortest_path = find_shortest_path(graph, start_node, end_node, num_nodes)
        print("The shortest path from node", start_node, "to node", end_node, "is", shortest_path)