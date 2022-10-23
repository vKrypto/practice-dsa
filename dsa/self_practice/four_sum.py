"""
https://leetcode.com/problems/4sum/submissions/
"""
class Solution:
    def twoSumPairs(self, nums: List[int], target) -> List[List[int]]:
        """
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
            
    
    def threeSum(self, nums: List[int], target=0) -> List[List[int]]:
        """
        copy form 3 sum
        """
        res = []
        for (k, v) in enumerate(nums):
            if k > 0 and nums[k-1] == v:
                continue
            for item in self.twoSumPairs(nums[k+1:], target - v):
                res.append([v] + item)
        return res
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Runtime: 102 ms, faster than 77.03% of Python3 online submissions for Median of Two Sorted Arrays.
        Memory Usage: 14.1 MB, less than 97.02% of Python3 online submissions for Median of Two Sorted Arrays.
        """
        nums.sort()
        res = []
        for (k, v) in enumerate(nums):
            if k > 0 and nums[k-1] == v:
                continue
            for item in self.threeSum(nums[k+1:], target-v):
                res.append([v] + item)
        return res