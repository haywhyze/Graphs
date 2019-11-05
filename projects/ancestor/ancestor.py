class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    
    def add_edge(self, v1, v2):
        if v1 not in self.vertices:
            self.add_vertex(v1) 
        if v2 not in self.vertices:
            self.add_vertex(v2)
        self.vertices[v2].add(v1)
    

    def dft(self, starting_vertex_id):
        # create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex_id)
        # create a set to store the visited vertices
        visited = set()
        my_list = []
        # while the stack is not empty
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()
            # if that vertex has not been visited
            if v not in visited:
                # mark it as visited
                my_list.append(v)
                visited.add(v)
                print(v)
                # then add all of it's neighbors to the top of the stack
                for next_vertex in sorted(self.vertices[v]):
                    s.push(next_vertex)
        return my_list[-1]

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for ancestor in ancestors:
        graph.add_edge(ancestor[0], ancestor[1])

    result = graph.dft(starting_node)
    if result == starting_node:
        return -1
    return result
