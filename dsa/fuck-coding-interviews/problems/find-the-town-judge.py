# https://leetcode.com/problems/find-the-town-judge/submissions/


from collections import defaultdict
from . import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(set)
        nodes = set(list(range(1,n+1)))
        for u,v in trust:
            graph[v].add(u)
            if u in nodes:
                nodes.remove(u)
        for node in nodes:
            if len(graph[node]) == n-1:
                return node
        return -1