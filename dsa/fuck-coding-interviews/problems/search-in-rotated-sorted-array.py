# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

class Solution:

    # time = o(n), sapce = o(1)
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2
            # base-case
            if target == nums[mid]:
                return mid
            
            # searching in left part
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # searching in right part 
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid-1
                
        return -1