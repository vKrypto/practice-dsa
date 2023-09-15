# https://leetcode.com/problems/min-cost-to-connect-all-points/
import sys
from typing import List

class Solution:

    @staticmethod
    def _dist(p1, p2):
      x1,y1 = p1
      x2, y2 = p2
      return abs(x2-x1) + abs(y2-y1)
    
    def build_graph(self, points):
        # build nxn grid points
        self.n = len(points)
        self.graph = [[0]*self.n for _ in range(self.n)]
        for i in range(self.n):
          for j in range(self.n):
            if i != j:
              self.graph[i][j] = self._dist(points[i], points[j])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.build_graph(points)
        parent = self.primMST()

        res = 0
        for i in range(1, self.n):
            res += self.graph[i][parent[i]]
        return res

    def minKey(self, key):
        min_val = sys.maxsize
        for v in range(self.n):
            if key[v] < min_val:
                min_val = key[v]
                min_index = v

        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.n
        parent = [None] * self.V 
        key[0] = 0
        mstSet = [False] * self.n

        parent[0] = -1 

        for _ in range(self.n):

            u = self.minKey(key)
            mstSet[u] = True
            for v in range(self.n):
                if self.graph[u][v] > 0 and mstSet[v] is False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
            key[u] = sys.maxsize
        return parent