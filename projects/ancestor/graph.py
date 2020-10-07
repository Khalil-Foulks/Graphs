"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # add vertex to vertices as an empty set if it doesn't exist alread
        if not self.vertices.get(vertex_id):
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # if keys exist in dictionary
        if v1 in self.vertices and v2 in self.vertices:
            # add v2 to v1's set
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def get_ancestor(self, starting_node):
        # if child has no parent
        if self.vertices[starting_node] == set():
            return -1
        
        s = Stack()
        visited = set()

        # add starting node to top of stack
        s.push(starting_node)
        # current pointer = starting node
        current = starting_node

        # while stack isn't empty
        while s.size() > 0:
            # remove from top of stack
            v = s.pop()

            # if node removed from stack hasn't been visited
            if v not in visited:
                # if size of stack isn't empty and there's no parent 
                if s.size() > 0 and self.vertices[v] == set():
                    # remove another node off of the stack 
                    v2 = s.pop()
                    # if 2nd removed node is smaller than 1st 
                    if v2 < v:
                        # use the smaller of the removed nodes; ignore the larger one
                        v = v2
                # print(v)
                # add removed node to visited
                visited.add(v)  
                # update current to removed node
                current =  v   
            for neighbor in self.get_neighbors(v):
                # push the neighbors to the top of stack
                s.push(neighbor)
        # return current node
        return current