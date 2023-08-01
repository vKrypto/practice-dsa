from collections import defaultdict
from typing import List


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(set)
        
    def addEdge(self, a, b):
        self.graph[a].add(b)
        self.graph[b].add(a)

    def _get_nodes_sort_by_degree(self) -> List:
        res = []
        for node in range(self.V):
            res.append((len(self.graph[node]), node))
        res.sort()    
        return res


    def graphColoring(self, m=None) -> None:
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

        print("assigned color: ", colors)
                


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

