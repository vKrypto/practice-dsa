import heapq
import sys

class Graph:
    
    def primMst(self):
        
        
        # dist = [(weight_of_edge_connected_to_mst, node)]
        queue = [(0, 0)]
        dist = [sys.maxsize for _ in range(self.n)]
        parent = [i for i in range(self.n)]
        
        for _ in range(self.n):
            
            _, node = heapq.pop(queue)
            
            for child_node, child_weight  in node.children:
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
            for child_node, child_weight  in node.children:
                # optimize dist[node][child_node]
                if child_node not in visited and dist[node] > child_weight:
                    dist[node] = child_weight
                    parent[child_node] = node
            if queue:
                rec(heapq.pop(queue))
        
        rec(0)        
        print(parent)