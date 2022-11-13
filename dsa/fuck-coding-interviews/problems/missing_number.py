# https://leetcode.com/problems/missing-number/
from typing import List


class Solution:
    """
    Runtime: 267 ms, faster than 50.80% of Python3 online submissions for Missing Number.
    Memory Usage: 15.2 MB, less than 79.82% of Python3 online submissions for Missing Number.
    """
    def missingNumber_2(self, nums: List[int]) -> int:
        n =len(nums)
        expected_sum = int(n * (n+1)/2)
        actual_sum= sum(nums)
        return expected_sum-actual_sum
    
    """
    Runtime: 370 ms, faster than 20.55% of Python3 online submissions for Missing Number.
    Memory Usage: 15.1 MB, less than 79.82% of Python3 online submissions for Missing Number.
    """
    def missingNumber_1(self, nums: List[int]) -> int:
        nums.sort()
        temp = -1
        for i in nums:
            if i == temp or i == temp+1:
                temp = i
            else:
                break
        return temp+1
    
    """
    Runtime: 169 ms, faster than 81.66% of Python3 online submissions for Missing Number.
    Memory Usage: 15 MB, less than 98.37% of Python3 online submissions for Missing Number.
    """
    def missingNumber(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        xor1, xor2 = 0, nums[0]
        for i in range(1, len(nums)+1):
            xor1 ^= i
        for i in range(1, len(nums)):
            xor2 ^= nums[i]
        return xor1 ^ xor2