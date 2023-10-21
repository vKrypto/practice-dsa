class Graph:
    
    def __init__(self) -> None:
        self.edges = [] # [(u,v, w)]
        self.parent = [-1] * self.n
        self.parent_mst = [-1] * self.n
        self.rank = [0]  * self.n
        self.total_weight = 0
        self.total_edges = 0
        
    def add_edge_to_mst(self, u, v, w):
        self.total_weight += w
        
        if self.rank[u] > self.rank[v]:
            self.parent[v] = u
        elif self.rank[u] < self.rank[v]:
            self.parent[v] = u
        else:
            self.parent[v] = u
            self.rank[v] += 1
            
    # o(1)
    def find_parent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]
    
    def mst(self):
        
        self.edges.sort(lambda x: x[2])
        
        
        while self.total_edges <= self.n-1:
            u,v, w = self.edges.pop(0)
            
            p_u = self.find_parent(u)
            p_v = self.find_parent(v)
            
            if p_u != p_v:
                self.add_edge_to_mst(u, v, w)
            else:
                print(" edges forming graph and also high weight")