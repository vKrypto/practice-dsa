# https://leetcode.com/problems/all-paths-from-source-to-target/

from . import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []

        n = len(graph)
        visited = [False] * n

        def dfs(node=0, parents=[]):
            visited[node] = True
            parents.append(node)
            if node == n-1:
                paths.append(parents)
                return
            
            for child in graph[node]:
                dfs(child, parents.copy())
        
        dfs()

        return paths

    # 60% beats in memory,  88.43% beats in performance
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        n = len(graph)

        def dfs(node=0, parents=[0]):
            if node == n-1:
                paths.append(parents)
            else:
                for child in graph[node]:
                    dfs(child, parents + [child])
        
        dfs()

        return paths
                
                