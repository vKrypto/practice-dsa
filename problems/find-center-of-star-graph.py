# https://leetcode.com/problems/find-center-of-star-graph/

from collections import defaultdict
from typinf import List

    
class Solution:

    # edge case-missing (when center is 3 points away from edge)
    def findCenter_1(self, e: List[List[int]]) -> int:    
        return e[0][e[0][1] in e[1]]
    
    def findCenter_0(self, e: List[List[int]]) -> int:    
        return (set(e[0]) & set(e[1])).pop()
        
    def findCenter(self, edges: List[List[int]]) -> int:
        self.graph = defaultdict(list)

        for (a, b) in edges:
            self.graph[a].append(b)
            self.graph[b].append(a)

        def dfs(node=1, path=[0]):
            # print("path", path)
            path.append(node)
            for child in self.graph[node]:
                if child == path[-2]:
                    continue
                else:
                    path = dfs(child, path)
                    break
            
            return path
        
        path = dfs()
        return path[len(path)//2]

