"""
url : https://leetcode.com/problems/first-missing-positive/
"""

from typing import List


class Solution:
    """
    time complexity : o (nlogn)
    Runtime: 1277 ms, faster than 35.89% of Python3 online submissions for First Missing Positive.
    Memory Usage: 63.2 MB, less than 41.45% of Python3 online submissions for First Missing Positive.
    """
    def firstMissingPositive_1(self, nums: List[int]) -> int:
        nums.sort()
        ans = 1
        for i in range(len(nums)):
            if nums[i] > 0:
                if nums[i] != ans and nums[i] >= ans:
                    return ans
                ans = min(ans +1, nums[i] + 1)
        return ans
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        time complexity : o (nlogn)
        Runtime: 661 ms, faster than 65.44% of Python3 online submissions for First Missing Positive.
        Memory Usage: 27.1 MB, less than 86.24% of Python3 online submissions for First Missing Positive.
        """
        nums.sort()
        ans = 1
        for v in nums:
            if v > 0:
                if v > ans:
                    return ans
                ans = min(ans +1, v + 1)
        return ans