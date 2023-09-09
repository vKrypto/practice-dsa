# https://leetcode.com/problems/k-closest-points-to-origin/submissions/960522129/
from typinf import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [(x**2 + y**2, x, y) for (x,y) in points]
        
        heapq.heapify(min_heap)

        res = []
        for _ in range(min(k, len(min_heap))):
            _, x, y = heapq.heappop(min_heap)
            res.append((x,y))
            
        return res