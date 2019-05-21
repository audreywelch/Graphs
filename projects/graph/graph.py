"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

# 0. Translate HOW this is a graph problem - understand
# 1. Build your graph 
# 2. Traverse your graph

## Part 1: Create a Graph Class
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        # Add a vertex to the graph.
        # Set to an empty set
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        # Add a directed edge to the graph.
        # Make sure v1 and v2 exist and are vertices
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    ## Part 2: Implement Breadth-First Traversal
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty Queue
        q = Queue()
        # Create an empty visited set
        visited_set = set()

        # Add the starting vertex to the queue
        q.enqueue(starting_vertex)

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex - take from the front of the array: vertices[0]
            first_vertex = q.dequeue()

            # If it has not been visited...
            if first_vertex not in visited_set:
                # Mark it as visited (print it and add it to the visited set)
                print(first_vertex)
                visited_set.add(first_vertex)
                # Then enqueue each of its neighbors in the queue
                for neighbor in self.vertices[first_vertex]:
                    q.enqueue(neighbor)

    ## Part 3: Implement Depth-First Traversal with a Stack
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # All we have to do is change the data structure from a queue to a stack
        # Create an empty Stack
        s = Stack()

        # Create an empty Visited set
        visited_set = set()

        # Push the starting vertex to the stack
        s.push(starting_vertex)

        # While the Stack is not empty...
        while s.size() > 0:
            # Pop the last vertex - take from the back of the array, the most recently added, which is what makes it go deep instead of wide: vertices[-1]
            vertex = s.pop()
            # If it has not been visited...
            if vertex not in visited_set:
                # Mark it as visited (print it and add it to the visited set)
                print(vertex)
                visited_set.add(vertex)
                # Then push each of its neighbors in the stack
                for neighbor in self.vertices[vertex]:
                    s.push(neighbor)

    ## Part 3.5: Implement Depth-First Traversal using Recursion
    def dft_recursive(self, starting_vertex, visited_set = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Need to do this because if we set it in the parameter as a default, it actually persists and then will only run once
        if visited_set is None:
            visited_set = set()
        # Mark the starting vertex as visited
        print(starting_vertex)
        visited_set.add(starting_vertex)

        # Call DFT_Recursive on each unvisited neighbor
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited_set:
                self.dft_recursive(neighbor, visited_set)


    ## Part 4: Implement Breadth-First Search
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order. (Guaranteed to give you the shortest path)
        """
        # Create an empty Queue
        q = Queue()

        # Create an empty visited set to store visited vertices
        visited_set = set()
        
        # enqueue A PATH TO the starting_vertex into the queue rather than storing just a vertex
        q.enqueue( [starting_vertex] )

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH from the front of the array
            path = q.dequeue()

            # Grab the last vertex of the PATH
            vertex = path[-1] # vertex is the last thing in the path array

            # Check if vertex is the destination we're searching for
            if vertex == destination_vertex:
                # If so, return the path
                return path

            # If it has not been visited...
            if vertex not in visited_set:

                # Mark it as visited (add it to the visited set)
                visited_set.add(vertex)
                # Then enqueue each PATHS TO each of its neighbors in the queue
                for neighbor in self.vertices[vertex]:
                    # Make a copy of the path, called new_path
                    path_copy = list(path) # OR you can set it to path.copy()
                    # Add the neighbor to the copy
                    path_copy.append(neighbor)
                    # Add the path copy to the queue
                    q.enqueue(path_copy)
        return None


    ## Implement Depth-First Search
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty Stack
        s = Stack()

        # Create an empty Visited set
        visited_set = set()

        # Push the PATH TO the starting vertex to the stack
        s.push( [starting_vertex] )

        # While the Stack is not empty...
        while s.size() > 0:
            # Pop the first PATH
            path = s.pop()

            # Grab the last vertex of the PATH
            vertex = path[-1]

            # Check if it's our destination
            if vertex == destination_vertex:
                return path

            # If it has not been visited...
            if vertex not in visited_set:

                # Mark it as visited (print it and add it to the visited set)
                print(vertex)
                visited_set.add(vertex)
                # Then push each of its neighbors in the stack
                for neighbor in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    s.push(new_path)
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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

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
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
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
