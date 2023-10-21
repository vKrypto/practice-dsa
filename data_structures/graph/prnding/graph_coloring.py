from collections import defaultdict
from typing import List


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

    def graphColoring_backtracking(self, m=0):
        if self._graphColorUtil(m, 0) is None:
            print("Backtrack Solution does not exist")
            return False
        else:
            print("assigned color using Backtrack: ", self.colors)
            return True

    def _get_nodes_sort_by_degree(self) -> List:
        res = []
        for node in range(self.V):
            res.append((len(self.graph[node]), node))
        res.sort()    
        return res

    def graphColoring_greedy(self, m=None) -> None:
        m = m or self.V

        colors = [-1]* self.V
        available_colors = [True]* m
        
        stack = self._get_nodes_sort_by_degree()
        
        while stack:
            _, node = stack.pop()
            # step 1: 
            for child in self.graph[node]:
                if colors[child] != -1:
                    available_colors[colors[child]] = False

            # step 2: color current node
            color = 0
            while color < m:
                if available_colors[color]:
                    colors[node] = color
                    break
                color += 1

            # step 3: base-case: make sure the node was colored            
            if colors[node] == -1:
                print("could not colored")
                return False

            # step 4: undo changes.
            for child in self.graph[node]:
                if colors[child] != -1:
                    available_colors[colors[child]] = True

        print("assigned color using    greedy: ", colors)

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
    g2.graphColoring_backtracking(3)
    g2.graphColoring_greedy(3)

