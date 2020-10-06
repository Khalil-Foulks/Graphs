from util import Stack, Queue
# from graph import Graph

nodes = {}

def earliest_ancestor(ancestors, starting_node):
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
        # if no acestor return -1

    for t in ancestors:
        parent = t[0]
        child = t[1]
        add_node(parent)
        add_node(child)
        add_edge(child, parent)
    print(nodes)


def add_node(node):
    nodes[node] = set()

def add_edge(node1, node2):
    # if node1 in nodes and node2 in nodes:
            # add node2 to node1's set
    nodes[node1].add(node2)

def get_neighbors(node):
    return nodes[node]

def dft(starting_vertex):
    q = Stack()
    visited = set()

    # Init - add starting node to top of stack
    q.push(starting_vertex)

    while q.size() > 0:
        # remove from the top of stack
        v = q.pop()

        if v not in visited:
            print(v) # visit the node

            # add to visited set
            visited.add(v)     

            # grab each neighbor of current vertex and add it to the top of stack 
            for neighbor in get_neighbors(v):
                q.push(neighbor) 

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 1)
