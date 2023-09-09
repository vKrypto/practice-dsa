"""
https://leetcode.com/problems/intersection-of-two-arrays/
"""
from typing import List

class Solution:
    
    def intersection_1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = set()
        res = set()
        for i in nums1:
            temp.add(i)
        for i in nums2:
            if i in temp:
                res.add(i)
        return res
         
