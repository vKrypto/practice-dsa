# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        time complexity: o(3n)
        space complexity: o(3n)
        Runtime: 369 ms, faster than 26.34% of Python3 online submissions for Product of Array Except Self.
        Memory Usage: 22.9 MB, less than 11.47% of Python3 online submissions for Product of Array Except Self.
        """
        n = len(nums)
        if n <=2:
            return nums[::-1]
        
        # initialize left_and right multiply array
        res = [0]*n
        left_mul = [0]*n
        right_mul = [0]*n
        left_mul[0] = 1
        right_mul[n-1] = 1
        
        # create left_mul
        for i in range(1,n):
            left_mul[i] = nums[i-1] * left_mul[i-1]
        
        # create right_mul
        for i in range(n-2, -1, -1):
            right_mul[i] = nums[i+1] * right_mul[i+1]
        
        for i in range(n):
            res[i] = left_mul[i] * right_mul[i]
        
        return res