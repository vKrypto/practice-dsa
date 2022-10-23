"""
https://leetcode.com/problems/3sum/submissions/
"""
from typing import List

class Solution:
    def twoSumPairs(self, nums: List[int], target) -> List[List[int]]:
        """
        time Complexity: o(n)
        copy from twoSum2 Problems
        """
        res = []
        l, r = 0, len(nums)-1
        while l< r:
            total = nums[l] + nums[r]
            if  total == target:
                res.append([nums[l], nums[r]])
            if total > target:
                r -= 1
            else:
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
        return res
            
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        time complexity: O(nlog(n)) + o(n^2)
        Runtime: 811 ms, faster than 81.68% of Python3 online submissions for 3Sum.
        Memory Usage: 17.9 MB, less than 82.22% of Python3 online submissions for 3Sum.
        """
        nums.sort()
        res = []
        for (k, v) in enumerate(nums):
            if k > 0 and nums[k-1] == v:
                continue
            for item in self.twoSumPairs(nums[k+1:], -v):
                res.append([v] + item)
        return res