import heapq
import sys

class Graph:
    def __init__(self, n:int) -> None:
        self.n = n
        self.graph = None
    
    def primMst(self):
        
        
        # dist = [(weight_of_edge_connected_to_mst, node)]
        queue = [(0, 0)]
        dist = [sys.maxsize for _ in range(self.n)]
        parent = [i for i in range(self.n)]
        
        for _ in range(self.n):
            
            _, node = heapq.heappop(queue)
            
            for child_node, child_weight  in self.graph[node]:
                # optimize dist[node][child_node]
                if dist[node] > child_weight:
                    dist[node] = child_weight
                    parent[child_node] = node
                    
        print(parent)
        
    def primMstRec(self):
        
        
        # dist = [(weight_of_edge_connected_to_mst, node)]
        queue = [(0, 0)]
        dist = [sys.maxsize for _ in range(self.n)]
        parent = [i for i in range(self.n)]
        visited = set()
                    
        def rec(node):
            # write terminate condition
            for child_node, child_weight  in self.graph[node]:
                # optimize dist[node][child_node]
                if child_node not in visited and dist[node] > child_weight:
                    dist[node] = child_weight
                    parent[child_node] = node
            if queue:
                rec(heapq.heappop(queue))
        
        rec(0)        
        print(parent)



# Driver's code
if __name__ == '__main__':
    g = Graph(5)
    g.graph = [[0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
    # convert g.graph to ajacency list
    g.graph = {key: [child_node for child_node, child_weight in enumerate(g.graph[key]) if child_weight] for key in range(len(g.graph))}
    g.primMst()

