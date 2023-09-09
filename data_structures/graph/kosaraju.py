# being used to get all strongly connected components

from collections import defaultdict

class Graph:
    def __init__(self,vertices):
            self.V= vertices 
            self.graph = defaultdict(list)

    def addEdge(self,u,v):
            self.graph[u].append(v)

    def _DFSUtil(self,v,visited):
        visited[v]= True
        print(v)
        for i in self.graph[v]:
            if not visited[i]:
                self._DFSUtil(i,visited)


    def _fillOrder(self,v,visited, stack):
        visited[v]= True
        for i in self.graph[v]:
            if not visited[i]:
                self._fillOrder(i, visited, stack)
        stack = stack.append(v)
        

    def _getTranspose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g

    def printSCCs(self):            
        stack = []
        visited =[False]*(self.V)
        
        # step 1:  Fill vertices in stack according to their finishing times
        for i in range(self.V):
            if not visited[i]:
                self._fillOrder(i, visited, stack)

        #step 2: Create a reversed graph
        gr = self._getTranspose()
            
        visited =[False]*(self.V)
        # step 3: Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if not visited[i]:
                gr._DFSUtil(i, visited)
                print("")

# Create a graph given in the above diagram
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)


print ("Following are strongly connected components " +
						"in given graph")
g.printSCCs()
