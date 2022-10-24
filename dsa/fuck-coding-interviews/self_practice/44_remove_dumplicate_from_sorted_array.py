"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
class Solution:
    def removeDuplicates(self, nums:list[int]) -> int:
        """
        Runtime: 99 ms, faster than 74.37% of Python3 online submissions for Remove Duplicates from Sorted Array.
        Memory Usage: 15.5 MB, less than 96.63% of Python3 online submissions for Remove Duplicates from Sorted Array.
        """
        count = 0
        for k, v in enumerate(nums):
            if not(k > 0 and nums[k] == nums[k-1]):
                nums[count] = v
                count += 1
        return count 
