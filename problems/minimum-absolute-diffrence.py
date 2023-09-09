# https://leetcode.com/problems/minimum-absolute-difference/description/
from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        """
        time: o(n(logn))
        Runtime: 376 ms, faster than 91.04% of Python3 online submissions for Minimum Absolute Difference.
        Memory Usage: 28.7 MB, less than 95.39%  of Python3 online submissions for Minimum Absolute Difference."""
        arr.sort()
        dp ={}
        min_diff = float('infinity')
        for k in range(1, len(arr)):
            diff = abs(arr[k]-arr[k-1])
            min_diff = min(diff, min_diff)
            if min_diff  == diff:
                if dp.get(diff) is None:
                    dp[diff] = []
                dp[diff].append([ arr[k-1], arr[k]])
        return dp[min_diff]