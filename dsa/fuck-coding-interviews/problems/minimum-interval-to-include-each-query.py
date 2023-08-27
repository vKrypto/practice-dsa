# https://leetcode.com/problems/minimum-interval-to-include-each-query/description/

from typing import List
import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = [-1] * len(queries)
        for j, query in enumerate(queries):
            min_dist = float('inf') 
            for interval in intervals:
                if query >= interval[0] and query <= interval[1]:
                    min_dist = min(min_dist, interval[1] - interval[0] + 1)
                if query < interval[0]:
                    break
            if min_dist != float('inf'):
                res[j] = min_dist
        return res

    # optimized version of
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]
