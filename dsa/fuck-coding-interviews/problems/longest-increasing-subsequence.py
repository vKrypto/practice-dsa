# https://leetcode.com/problems/longest-increasing-subsequence/
from typing import List


class Solution:
    
    # cached recursion
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def rec(i=0, last_num=None):
            if i >=  len(nums):
                return 0
            if (i, last_num) in cache:
                return cache[(i, last_num)]
            way_1 = 0
            # take it 
            if last_num is None or last_num < nums[i]:
                way_1 = 1 + rec(i+1, nums[i])
            way_2 = rec(i+1, last_num)
            cache[(i, last_num)] = max(way_1, way_2)
            return max(way_1, way_2)

        return rec()
    
    
    # 2516 ms, faster than 64.96%
    # space optimized tabular solution
    def lengthOfLIS_1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)