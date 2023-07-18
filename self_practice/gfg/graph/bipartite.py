class Graph:
    
    
    def __init__(self, vertices=5) -> None:
        self.n = vertices
        self.graph = None
        self.visited = [None]* self.n
        self.color = [None]* self.n
    
    
    def bipartite(self, node=0, color=0):
        self.color[node]=color
        self.visited[node] = 1
        for child_node, child_weight in enumerate(self.graph[node]):
            if child_weight != 0 and not self.visited[child_node]:
                if self.bipartite(child_node, color^1):
                    return False
            if self.color[child_node] == color:
                return False
        return True
                
            
            

# Driver's code
if __name__ == '__main__':
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    print(g.bipartite())

