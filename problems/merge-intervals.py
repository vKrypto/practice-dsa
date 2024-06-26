# coding: utf-8
"""
https://leetcode.com/problems/merge-intervals/
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])

        first_pair = intervals[0]
        output = [first_pair, ]
        for pair in intervals[1:]:
            last_merged_pair = output[-1]

            # if the current pair's low is greater than the last merged pair's high
            # it must be a new interval
            if pair[0] > last_merged_pair[1]:
                output.append(pair)
                continue

            if pair[1] > last_merged_pair[1]:
                last_merged_pair[1] = pair[1]

        return output
 
    # time: o(n), space: o(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                # merge
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
