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
        if self.vertices.get(starting_node) == set():
            return -1
        
        s = Stack()
        visited = set()
        # path = [starting_node]

        s.push(starting_node)
        current = starting_node

        while s.size() > 0:
            v = s.pop()

            if v not in visited:
                if self.vertices.get(starting_node) == set():
                    v2 = s.pop()
                    if v2 < v:
                        v = v2
                # print(v)
                visited.add(v)  
                current =  v   
            for neighbor in self.get_neighbors(v):
                s.push(neighbor)
        return current        
