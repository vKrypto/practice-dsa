# https://leetcode.com/problems/find-center-of-star-graph/

from collections import defaultdict
from . import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            if graph[v]:
                return v
            if graph[u]:
                return u
            graph[u].append(v)
            graph[v].append(u)