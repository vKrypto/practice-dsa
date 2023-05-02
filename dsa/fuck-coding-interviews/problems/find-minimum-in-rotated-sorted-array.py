# coding: utf-8
"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""
from typing import List
import sys


class Solution:
    def findMin(self, nums: List[int]) -> int:
        last_num = -sys.maxsize
        for num in nums:
            if num < last_num:
                return num
            else:
                last_num = num

        return nums[0]


class Solution2:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]

        low = 0
        high = len(nums) - 1
        first_value = nums[0]
        while low <= high:
            # The array is not roated
            if nums[low] < nums[high]:
                return first_value

            mid = int((low + high) / 2)
            mid_value = nums[mid]

            # ex: [3, 4, 5, 1, 2]
            if mid_value > nums[mid + 1]:
                return nums[mid + 1]

            # ex: [3, 1, 2]
            if mid_value < nums[mid - 1]:
                return mid_value

            # The left side of the middle is sorted,
            # so we should check the right side of the middle
            # ex: [1, 2, 4, 5, 6, 7, 0]
            if first_value < mid_value:
                low = mid + 1

            # The right side of the middle is sorted,
            # so we should check the left side of the middle
            # ex: [7, 0, 1, 2, 4, 5, 6]
            if first_value > mid_value:
                high = mid - 1
