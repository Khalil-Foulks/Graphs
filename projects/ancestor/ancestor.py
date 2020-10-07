from util import Stack, Queue
from graph import Graph

g = Graph()

def earliest_ancestor(ancestors, starting_node):

    for t in ancestors:
        parent = t[0]
        child = t[1]
        g.add_vertex(parent)
        g.add_vertex(child)
        g.add_edge(child, parent)
    print(g.vertices)
    return g.get_ancestor(starting_node)           


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 3))






# earliest = furthest use (dft/dfs)

# INIT
    # create a dictionary to store nodes
        # each key in dictionary is a child node
        # each value is a parent node of child

# ADD VERTEX & EDGE - make the child the key and the parent in the set 
    # loop through ancestors list to grab (P, C) tuple
        # each 0 index is a parent in value in set
        # each 1 index is a key

# GET NEIGHBORS

# DFT
    # create a empty stack
    # create empty visited set
    # push start node to top of stack
    # while stack is > 0 
    # remove from top of stack
    # if node hasn't been visited
    # add it to visited
    # push neighbors  to top of stack
    # repeat till stack is empty
    # if length of dictionary - length of visited = 1 (I'm at the last unvisted node)
        # return last node (this must be the furthest ancestor)
    # if no ancestor return -1