from collections import defaultdict


class Graph:
    def __init__(self, node_count) -> None:
        self.node_count = node_count
        self.graph =[[]] 
        

    def has_cycle(self):
        visited = [False] * self.node_count
        
        def dfs(node=0, parent=None):
            visited[node] = True
            for child, weight in enumerate(self.graph[node]):
                if weight:
                    if not visited[child]:
                        visited[child] = True
                        dfs(child, parent=node)
                    elif child != parent:
                        return True
            return False
        
        return dfs()
                            
class DisjointSetGraph:
    
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.parent = [-1] * n
        self.edges = []

    def find(self, node):
        if self.parent[node] < 0:
            return node
        else:
            parent = self.find(self.parent[node])
            self.parent[node] = parent
            return parent
        
    
    def add_edge(self, edge):
        self.edges.append(edge)
        from_node, to_node = edge
        self.graph[from_node].append(to_node)
        a = self.find(from_node)
        b = self.find(to_node)
        if a == b:
            return            
        #  both belong to the different family
        weight_a = self.parent[a]
        weight_b = self.parent[b]

        # may need to update all member's parent
        if weight_a > weight_b:
            self.parent[a] = weight_a + weight_b
            self.parent[b] = a 
        elif weight_a < weight_b:
            self.parent[b] = weight_a + weight_b
            self.parent[a] = b 
        else:
            self.parent[a] = weight_a + weight_b
            self.parent[b] = a
    
    def remove_edge(self, edge):
        pass
    
    def find_bridge(self):
        bridges = []
        for edge in self.edges:
            self.remove_edge(edge)            
            from_node, to_node = edge
            parent_from = self.find(from_node)
            parent_to = self.find(to_node)
            if parent_from != parent_to:
                bridges.append(edge)
        return bridges
    
# Driver Code
if __name__ == '__main__':
    g2 = DisjointSetGraph(5)
    g2.addEdge(0, 1)
    g2.addEdge(0, 2)
    g2.addEdge(1, 2)
    g2.addEdge(1, 4)
    g2.addEdge(2, 4)
    g2.addEdge(4, 3)

    g2.find_bridges()

                
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

    print(g.has_cycle())

