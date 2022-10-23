# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List

class Solution:
    """
    Runtime: 231 ms, faster than 78.73% of Python3 online submissions for Longest Consecutive Sequence.
    Memory Usage: 23.3 MB, less than 98.17% of Python3 online submissions for Longest Consecutive Sequence.
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        l = 0
        r = 0
        temp = 1 # local max
        max_length = 1 # global max
        for i, v in enumerate(nums):
            if i > 0  and( v == nums[i-1]+1 or  v == nums[i-1]):
                if  v == nums[i-1]:
                    continue
                temp += 1
                r = i
            else:
                l = r = i
                max_length = max(max_length, temp)
                temp = 1
        return max(max_length, temp)
        
