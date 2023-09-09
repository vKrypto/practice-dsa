# Python program to print transitive
# closure of a graph.
from collections import defaultdict

class Graph:

    def __init__(self,vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

        # To store transitive closure
        self.tc = [[0 for j in range(self.V)] for i in range(self.V)]

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive DFS traversal function that finds
    # all reachable vertices for s
    def DFSUtil(self, s, v):

        # Mark reachability from s to v as true.
        if(s == v):
            print(s, v, self.graph[s])
            if( v in self.graph[s]):
                self.tc[s][v] = 1
        else:
            self.tc[s][v] = 1

        # Find all the vertices reachable through v
        for i in self.graph[v]:
            if self.tc[s][i] == 0:
                if s==i:
                    self.tc[s][i]=1
                else:
                    self.DFSUtil(s, i)

    # The function to find transitive closure. It uses
    # recursive DFSUtil()
    def transitiveClosure(self):
        print(self.graph)
        # Call the recursive helper function to print DFS
        # traversal starting from all vertices one by one
        for i in range(self.V):
            self.DFSUtil(i, i)
        
        print(self.tc)

# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.transitiveClosure()
