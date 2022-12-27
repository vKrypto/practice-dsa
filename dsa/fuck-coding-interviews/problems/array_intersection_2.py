"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""
from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        # make sure nums2 is smallest
        if len(nums1) <len(nums2):
            nums1, nums2 = nums2, nums1
        
        # store a counter mapping
        map_2 = Counter(nums2)

        # iterate over nums1 and check for intersection in map_2
        for i in nums1:
            # if found, decrease count, and add to result
            if map_2.get(i):
                result.append(i)
                map_2[i] -= 1

        return result