# https://leetcode.com/problems/insert-interval/submissions/

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # case 1: new interval is before cur interval and not overlapping. 
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # case 2: new interval is after cur interval and not overlapping. 
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # case3: overlapping, just merge cur with new
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res
