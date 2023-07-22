class Solution:

    def find_longest_distance(self, edges, q, query):
        graph = {}
        for edge in edges:
            u, v, w = edge
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append((v, w))
            graph[v].append((u, w))

        def dfs(node, parent, distance, memo):
            if (node, parent) in memo:
                return memo[(node, parent)]

            max_distance = distance
            for neighbor, edge_distance in graph[node]:
                if neighbor != parent:
                    max_distance = max(max_distance, dfs(neighbor, node, distance + edge_distance, memo))

            memo[(node, parent)] = max_distance
            return max_distance

        longest_distances = []
        for start_city in query:
            memo = {}
            longest_distances.append(dfs(start_city, None, 0, memo))

        return longest_distances
        
edges = [[1, 5, 3],
             [2, 5, 3],
             [1, 4, 2],
             [5, 3, 2]]
print(Solution().find_longest_distance(edges, 4,  [1, 3, 4, 5]))