# https://leetcode.com/problems/redundant-connection/description/
from collections import defaultdict
from typing import List


class DisjointSetGraph:
    
    def __init__(self):
        self.parent = defaultdict(lambda: -1)

    def find(self, node):
        if self.parent[node] < 0:
            return node
        else:
            parent = self.find(self.parent[node])
            self.parent[node] = parent
            return parent
        
    
    def add_edge(self, edge):
        from_node, to_node = edge
        a = self.find(from_node)
        b = self.find(to_node)
        if a == b:
            return  False
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
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        g = DisjointSetGraph()
        res = None
        for edge in edges:
            if not g.add_edge(edge):
                res = edge
        return res


