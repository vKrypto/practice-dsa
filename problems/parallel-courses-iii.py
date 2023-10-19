from collections import defaultdict
from typing import List
# https://leetcode.com/problems/parallel-courses-iii/description/


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # Build an adjacency list to represent the graph
        graph = defaultdict(list)
        for u, v in relations:
            graph[v - 1].append(u - 1)

        # Create an array to store the maximum time for each node
        max_time = [0] * n

        def dfs(node):
            if max_time[node] > 0:
                return max_time[node]

            max_child_time = 0
            for child in graph[node]:
                max_child_time = max(max_child_time, dfs(child))

            max_time[node] = max_child_time + time[node]
            return max_time[node]

        global_max = 0
        for i in range(n):
            global_max = max(global_max, dfs(i))

        return global_max
