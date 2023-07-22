from typing import List

from collections import defaultdict
class Solution:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}

        self.graph[u][v] = w
        self.graph[v][u] = w

    def longest_route_from_node(self, node, visited):
        visited[node] = True
        max_depth = 0

        for neighbor, weight in self.graph[node].items():
            if not visited[neighbor]:
                max_depth = max(max_depth, self.longest_route_from_node(neighbor, visited) + weight)

        return max_depth

    def longDrive(self, n, edges, q, query):
        for u, v, w in edges:
            self.add_edge(u, v, w)

        res = []
        for i in query:
            visited = {node: False for node in self.graph}
            res.append(self.longest_route_from_node(i, visited))

        return res

        
edges = [[1, 5, 3],
             [2, 5, 3],
             [1, 4, 2],
             [5, 3, 2]]
print(Solution().longDrive(n=6, edges=edges, q=4,  query=[1, 3, 4, 5]))