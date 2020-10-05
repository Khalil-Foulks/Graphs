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
                print('bft:', v) # visit the node

                # add to visited set
                visited.add(v)

                # grab each neighbor of current vertix and add it to the queue 
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        q = Stack()
        visited = set()
    
        # Init - add starting node to top of stack
        q.push(starting_vertex)

        while q.size() > 0:
            # remove from the top of stack
            v = q.pop()

            if v not in visited:
                print('dft:', v) # visit the node

                # add to visited set
                visited.add(v)     

                # grab each neighbor of current vertex and add it to the top of stack 
                for neighbor in self.get_neighbors(v):
                    q.push(neighbor)           



    def dft_recursive(self, starting_vertex,visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        q = Stack()
        

        if visited is None:
            visited = set()
    
        # Init - add starting node to top of stack
        q.push(starting_vertex)

        while q.size() > 0:
            # remove from the top of stack
            v = q.pop()

            if v not in visited:
                print('dft_re:', v) # visit the node

                # add to visited set
                visited.add(v)     

                # grab each neighbor of current vertex and add it to the top of stack 
                for neighbor in self.get_neighbors(v):
                    # calls function again on neighbors while travesing and keeps track of visted vertices
                    self.dft_recursive(neighbor, visited)  



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

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
