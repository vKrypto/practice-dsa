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
        temp = 1 # local max
        max_length = 1 # global max
        for i, v in enumerate(nums):
            if i > 0  and( v == nums[i-1]+1 or  v == nums[i-1]):
                if  v == nums[i-1]:
                    continue
                temp += 1
            else:
                max_length = max(max_length, temp)
                temp = 1
        return max(max_length, temp)


    # time: o(n), space: o(n)
    def longestConsecutive(self, nums: List[int]) -> int: 
        # base-case:
        if not nums:
            return 0
        nums_set = set()
        for i in nums:
            nums_set.add(i)
        res = 1
        for i in nums_set:
            if i-1 in nums_set:
                continue
            else:
                local_res = 1
                while i+1 in nums_set:
                    local_res += 1
                    i = i+1
                res = max(res, local_res)

        return res