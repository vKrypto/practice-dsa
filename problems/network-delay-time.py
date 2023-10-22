import sys
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def dij(self, source=0):
        distance = [sys.maxsize for i in range(self.node_count+1)]
        visited = [False for i in range(self.node_count+1)]
        
        queue = [(0, source)]
        distance[source] = 0
        while queue:
            cur_dist, cur_node = heapq.heappop(queue)
            visited[cur_node] = True
            for neighbor_node, neighbor_node_dist  in self.graph[cur_node]:
                total_distance = cur_dist + neighbor_node_dist
                if total_distance <= distance[neighbor_node]:
                    distance[neighbor_node] = total_distance
                    if not visited[neighbor_node]:
                        heapq.heappush(queue, (total_distance, neighbor_node))
        return distance

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.node_count = n
        self.graph = defaultdict(set)
        for (u, v , w) in times:
            self.graph[u].add((v, w))

        dist = self.dij(k)
        # print(dist)
        res = 0
        for i in dist[1:]:
            if i == sys.maxsize:
                return -1
            res = max(res, i)

        return res or -1
        