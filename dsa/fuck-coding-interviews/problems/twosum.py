"""
https://leetcode.com/problems/two-sum/
"""
from typing import List


class Solution:
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        """
        method 1: Bruteforce
        Runtime: 3755 ms, faster than 27.00% of Python3 online submissions for Two Sum.
        Memory Usage: 14.8 MB, less than 99.53% of Python3 online submissions for Two Sum.
        """
        l = len(nums)
        for i in range(l):
            for j in range(i, l):
                s = nums[i] + nums[j]
                if s == target and i != j:
                    return [i,j]
                
    def twoSumHashMap(self, nums: List[int], target: int) -> List[int]:
        """
        Method 2: Using HashMap
        Runtime: 59 ms, faster than 94.60% of Python3 online submissions for Two Sum.
        Memory Usage: 15.2 MB, less than 50.42% of Python3 online submissions for Two Sum.  
        """
        dp = {} # val: index
        for i,v in enumerate(nums):
            looking_for_index = dp.get(target - v)
            if looking_for_index is not None:
                return [looking_for_index, i]
            else:
                dp[nums[i]] = i
