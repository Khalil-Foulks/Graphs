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
                print(v) # visit the node

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
        if visited is None:
            visited = set()
    
        if starting_vertex not in visited:
            print(starting_vertex) # visit the node

            # add to visited set
            visited.add(starting_vertex)     

            # grab each neighbor of current vertex and add it to the top of stack 
            for neighbor in self.get_neighbors(starting_vertex):
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
        q = Stack()
        # init path as array containing the starting vertex
        path = [starting_vertex]
        
        # add the path to the stack
        q.push(path)        
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:
            # remove from the top of the stack
            v = q.pop()
            # store the last vertex from path that was just removed from the stack
            last_vertex = v[-1]
            # if last vertex matches 
            if last_vertex == destination_vertex:
                # return the path
                return v 
            # otherwise 
            else:
                # add the  lasat vertex to visited
                visited.add(last_vertex)
                
                # grab the neighbors, for each neighbor
                for neighbor in self.get_neighbors(last_vertex):
                    # copy path removed from stack
                    path = v[:]
                    # add path to stack
                    q.push(path)
                    # add the neighbor to the path, continue searching
                    path.append(neighbor)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        if visited is None:
            visited = set()

        if path is None:
            path = [] 
        
        # copy path append starting vertex
        path = path + [starting_vertex] 
        
        # add current vertex to visited and path
        visited.add(starting_vertex)

        # if current vertex is destination vertex, return path
        if starting_vertex == destination_vertex:
            return path 
        else:
            # grab each neighbor of current vertex
            for neighbor in self.get_neighbors(starting_vertex):
                if neighbor not in visited:
                    # re run function using the neighbor as starting vertex, pass down visted and path
                    re_path = self.dfs_recursive(neighbor, destination_vertex, visited, path) 
                    if re_path:
                        return re_path
            # did not find path
            return None


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
