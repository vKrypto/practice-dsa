class Solution:

    def longest_route_from_node(self, node, visited):
        visited[node] = True
        max_depth = 0

        for u, v, weight in self.edges:
            if u == node and not visited[v]:
                max_depth = max(max_depth, self.longest_route_from_node(v, visited) + weight)
            elif v == node and not visited[u]:
                max_depth = max(max_depth, self.longest_route_from_node(u, visited) + weight)

        return max_depth

    def longDrive(self, n, edges, q, query):
        self.edges = edges
        res = []
        for i in query:
            visited = {node: False for node in range(1, n+1)}
            res.append(self.longest_route_from_node(i, visited))

        return res

        
edges = [[1, 5, 3],
             [2, 5, 3],
             [1, 4, 2],
             [5, 3, 2]]
print(Solution().longDrive(n=6, edges=edges, q=4,  query=[1, 3, 4, 5]))