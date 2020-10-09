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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()

        # init - add starting node to queue
        q.enqueue(starting_vertex)

        # while queue isnt empty
        while q.size() > 0:
            # removed vertex from queue
            v = q.dequeue()

            # check if it exist in the visited set
            if v not in visited:
                print(v) # visit the node

                # add to visited set
                visited.add(v)

                # grab each neighbor of current vertix and add it to the queue 
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
		# Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        path = [starting_vertex]

        q.enqueue(path)
		# Create a Set to store visited vertices
        visited = set()
		# While the queue is not empty...
        while q.size() > 0:
			# Dequeue the first PATH
            v = q.dequeue()
			# Grab the last vertex from the PATH
            last_vertex = v[-1]
			# If that vertex has not been visited...
            if last_vertex == destination_vertex:
				# CHECK IF IT'S THE TARGET
				  # IF SO, RETURN PATH
                  return v
            else:
				# Mark it as visited...
                visited.add(last_vertex)
				# Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last_vertex):
                    # COPY THE PATH
                    path = v[:]
                    q.enqueue(path)
                    # APPEND THE NEIGHOR TO THE BACK
                    path.append(neighbor)