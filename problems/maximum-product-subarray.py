from typing import List

'''Leetcode - https://leetcode.com/problems/maximum-product-subarray/'''

'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Input: nums = [2,3,-2,4]
Output: 6
'''

# Solution1

# T:O(N^2)
# S:O(1)

# Solution2
def maxProduct(nums):
    if(len(nums)) == 0:
        return 0
    curr_max = nums[0]
    curr_min = nums[0]
    result = curr_max

    for i in range(len(nums)):
        curr = nums[i]
        temp_max = max(curr, curr_max*curr_min*curr)
        curr_min = min(curr, curr_max*curr_min*curr)
        curr_max = temp_max
        result = max(curr_max, result)
    return result

# T:O(N)
# S:O(1)


class Solution:
    def maxProduct(nums):
        """
        brute-force solution
        """
        if(len(nums)) == 0:
            return 0
        maxp = nums[0]
        for i in range(len(nums)):
            currp = 1
            for j in range(i, len(nums)):
                currp *= nums[j]
                maxp = max(maxp, currp)
        return maxp


    def maxProduct(self, nums: List[int]) -> int:
        """
        iterative solution
        """
        global_max = max(nums)

        local_max = 1
        local_min = 1
        for i in nums:
            if i ==0:
                local_max = 1
                local_min = 1
                continue
            min_temp = max(local_min * i, local_max * i)
            max_temp = min(local_min * i, local_max * i)

            local_max = max(max_temp, min_temp, i)
            local_min = min(max_temp, min_temp, i)

            global_max = max(local_max, global_max)
        return global_max

    def maxProduct(self, nums: List[int]) -> int:
        """
        recursive solution
        """
        g_max = [float('-inf')]
        def rec(index):
            if index > len(nums)-1:
                return 1, 1
            i = nums[index]
            _max, _min = rec(index+1)
            if i==0:
                res = 0, 0
            else:
                res = max(_max*i, _min*i, i), min(_max*i, _min*i, i)
            g_max[0] = max(g_max[0], *res)
            return res
        
        rec(0)
        return g_max[0]