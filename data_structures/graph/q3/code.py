from collections import defaultdict
from functools import lru_cache

class Solution:

    def longDrive(self, edges, query):
        if not (isinstance(edges, list) or isinstance(query, list)):
            raise TypeError('edges and query must be lists')
        
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        visited = set()
        @lru_cache(maxsize=None)
        def _dfs(node, parent):
            max_distance = 0
            for neighbor, edge_distance in graph[node]:
                if neighbor not in visited and neighbor != parent:
                    visited.add(neighbor)
                    max_distance = max(max_distance, _dfs(neighbor, node) + edge_distance)
                    visited.remove(neighbor)

            return max_distance

        return [_dfs(start_city, None) if start_city in graph else 0 for start_city in query]

        
        

edges = [[1, 5, 3],
             [2, 5, 3],
             [1, 4, 2],
             [5, 3, 2]]
print(Solution().longDrive(edges,  [1, 3, 4, 5]))