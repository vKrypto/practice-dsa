from collections import defaultdict


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.colors = [-1] * self.V
        
    def addEdge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def isSafe(self, v, c):
        for child in self.graph[v]:
            if self.colors[child] == c:
                return False
        return True

    def _graphColorUtil(self, m, v=0):
        for c in range(m):
            # check if safe decision
            if self.isSafe(v, c):
                # step 1: add a step
                self.colors[v] = c 
                # step 2: go deeper
                if  v == self.V-1 or self._graphColorUtil(m, v + 1):
                    return True
                # step 3: backtrack if wrong decision
                self.colors[v] = 0

    def graphColoring(self, m=0):
        if self._graphColorUtil(m, 0) is None:
            print("Solution does not exist")
            return False
        else:
            print("Solution exist and Following are the assigned colors:")
            print(self.colors)
            return True


# Driver Code
if __name__ == '__main__':
    g2 = Graph(5)
    g2.addEdge(0, 1)
    g2.addEdge(0, 2)
    g2.addEdge(1, 2)
    g2.addEdge(1, 4)
    g2.addEdge(2, 4)
    g2.addEdge(4, 3)

    # Function call
    g2.graphColoring(3)

