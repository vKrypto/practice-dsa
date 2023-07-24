# https://leetcode.com/problems/find-if-path-exists-in-graph/

from . import List
from collections import defaultdict

class Solution:
    def validPath(self, n: int, 
                  edges: List[List[int]], source: int, destination: int) -> bool:
        # form source node go dfs recursively, use visited to avoid cycles.
        
        # step1: generate adjacency list
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # step 2: crawl graph with recursive dfs
        visited = [False] * n
        def dfs(node=source):
            if node==destination:
                return True
            visited[node] = True
            for child in graph[node]:
                if not visited[child]:
                    if dfs(child):
                        return True
            return False        
        return dfs()
    
    def validPath(self, n: int, 
                  edges: List[List[int]], source: int, destination: int) -> bool:
        # form source node go dfs recursively, use visited to avoid cycles.
        
        # step1: generate adjacency list
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)


        # step 2: crawl graph with iterative dfs
        visited = [False] * n
        stack = [source]
        while stack:
            node = stack.pop()
            if node==destination:
                return True
            visited[node] = True
            for child in graph[node]:
                if not visited[child]:
                    stack.append(child)
        return False