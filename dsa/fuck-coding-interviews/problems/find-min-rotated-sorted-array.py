# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        r, l = 0, n-1
        mid = (r+l)//2
        res = nums[0]
        while r <= l:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (r+l)//2
            res = min(res, nums[mid])
            if nums[l] < nums[mid]:
                l = mid+1
            else:
                r = mid-1

        return res
    