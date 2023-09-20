# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/
from typing import List


class Solution:
    def minOperations_rec(self, nums: List[int], x: int) -> int:
        total =  sum(nums)
        if total == x:
            return len(nums)
        if total < x:
            return -1

        n  = len(nums)
        i = 0
        j = n-1

        def rec(i, j, k, c):
            if i >= n or j < 0 or i > j:
                return float('inf')
            c += 1
            if k == nums[i] or k == nums[j]:
                return c

            case_1 = rec(i+1, j, k-nums[i], c)
            case_2 = rec(i, j-1, k-nums[j], c)

            return min(case_1, case_2)

        res = rec(i, j, x, 0)
        return -1 if res == float('inf') else res

    def minOperations(self, nums: List[int], x: int) -> int:
        target, n = sum(nums) - x, len(nums)
        
        if target == 0:
            return n
        
        max_len = cur_sum = left = 0
        
        for right, val in enumerate(nums):
            cur_sum += val
            while left <= right and cur_sum > target:
                cur_sum -= nums[left]
                left += 1
            if cur_sum == target:
                max_len = max(max_len, right - left + 1)
        
        return n - max_len if max_len else -1