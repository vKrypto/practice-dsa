from typing import List
# https://leetcode.com/problems/product-of-array-except-self/

# T:O(N)
# S:O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left product array
        n = len(nums)

        res = [1] * n
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        
        
        last = 1
        for i in range(n-2, -1, -1):
            last *= nums[i+1]
            res[i] *= last

        return res