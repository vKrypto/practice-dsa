class Graph:
    
    
    def __init__(self, vertices=5) -> None:
        self.n = vertices
        self.graph = None
        self.color = [None]* self.n
    
    
    def bipartite(self, node=0, color=0):
        self.color[node]=color
        for child_node, child_weight in enumerate(self.graph[node]):
            if child_weight == 0:
                continue
            if self.color[node] is None:
                if self.bipartite(child_node, color^1):
                    return False
            if self.color[child_node] == color:
                return False
        return True
             
    def bipartite_recursive_bfs(self, queue=[0], color=0):
        if not queue:
            return True
        next_level = []
        for node in queue:
            for child_node, child_weight in enumerate(self.graph[node]):
                if child_weight == 0:
                    continue
                elif self.color[node] is None:
                    self.color[node]=color^1
                    next_level.append(child_node)
                elif self.color[child_node] == color:
                    return False
        return self.bipartite_recursive_bfs(next_level, color^1)
            

# Driver's code
if __name__ == '__main__':
    g = Graph(4)
    g.graph = [[0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]]

    # print(g.bipartite())
    g.color[0]= 0
    print(g.bipartite_recursive_bfs([0], 0))

