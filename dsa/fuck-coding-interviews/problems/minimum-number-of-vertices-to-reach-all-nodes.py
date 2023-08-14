# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/description/

from typinf import List


    
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        self.parent = [-1] * n
        in_degree_nodes = [False]*n
        for (from_node, to_node) in edges:
            in_degree_nodes[to_node] = True

        res = []
        for node, val in enumerate(in_degree_nodes):
            if not val:
                res.append(node)
        
        return res