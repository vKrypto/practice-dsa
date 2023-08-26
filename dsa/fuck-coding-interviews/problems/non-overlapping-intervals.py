# https://leetcode.com/problems/non-overlapping-intervals/description/
from typing import List


class Solution:
    
    # time:O(n), space:O(1)
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        res = 0
        prev = intervals[0]
        for i in range(1,  len(intervals)):
            cur = intervals[i]
            # if overlap
            if cur[0] < prev[1]:
                res += 1
                if prev[1] > cur[1]:
                    prev = cur
            else:
                prev = cur
        return res