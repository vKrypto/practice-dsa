# https://leetcode.com/problems/find-the-town-judge/submissions/


from collections import defaultdict
from . import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(int)
        nodes = set(range(1,n+1))
        for u,v in trust:
            graph[v].append(u)
            if u in nodes:
                nodes.remove(u)
        for node in nodes:
            if len(graph[node]) == n-1:
                return node
        return -1
    

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(int)
        nodes = set(range(1,n+1))
        for u,v in trust:
            graph[v] += 1
            if u in nodes:
                nodes.remove(u)
        for node in nodes:
            if graph[node] == n-1:
                return node
        return -1
    
    
    # 98% beats in memory, 96% in cpu 
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(int)
        nodes = [False] * (n + 1)
        for u,v in trust:
            graph[v] += 1
            if not nodes[u]: 
                nodes[u] = True
        for node, val in enumerate(nodes):
            if node != 0 and not val and graph[node] == n-1:
                return node
        return -1