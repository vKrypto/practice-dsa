# https://leetcode.com/problems/find-triangular-sum-of-an-array/
from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        """
        Runtime: 2703 ms, faster than 80.47% of Python3 online submissions for Find Triangular Sum of an Array.
        Memory Usage: 13.9 MB, less than 95.03% of Python3 online submissions for Find Triangular Sum of an Array.
        """
        while len(nums) != 1:
            temp = []
            for i in range(len(nums)-1):
                num = nums[i] + nums[i+1]
                temp.append(num%10)
            nums=temp
        
        return nums[0] 
    