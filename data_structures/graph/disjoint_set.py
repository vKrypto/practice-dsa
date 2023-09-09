# grouping_graph_nodes with parent nodes

from collections import defaultdict

class DisjointSetGraph:
    
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.parent = [-1] * n

    def find(self, node):
        if self.parent[node] < 0:
            return node
        else:
            parent = self.find(self.parent[node])
            self.parent[node] = parent
            return parent
        
    
    def add_edge(self, edge):
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
    
    
    
    

# Driver's code
if __name__ == '__main__':
    g = DisjointSetGraph(6)
    edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
    for edge in edges:
        g.add_edge(edge)
