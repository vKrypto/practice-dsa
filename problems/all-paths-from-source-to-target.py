# https://leetcode.com/problems/all-paths-from-source-to-target/

from typinf import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # ignore cyclic paths as questions  SAYS it's acyclic DAG
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


    # backtrack - method
    def allPathsSourceTarget_1(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        source = 0
        target = n-1
        res = []
        path = []
        def dfs(node=source):
            if node == target:
                res.append([0] + path.copy())
                return
            
            for child_node in graph[node]:
                path.append(child_node)
                dfs(child_node)
                path.pop()

        dfs()
        return res


    # recursion - method
    def allPathsSourceTarget_2(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        source, target = 0, n-1
        res = []

        def dfs(node=source, path=[0]):
            if node == target:
                res.append(path)
                return
            
            for child_node in graph[node]:
                dfs(child_node, path + [child_node])

        dfs()
        return res