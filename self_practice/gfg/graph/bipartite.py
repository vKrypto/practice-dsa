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
                
                