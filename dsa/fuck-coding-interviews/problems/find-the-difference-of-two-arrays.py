# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/
from . import List, Counter


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # use-case: item frequency matters
        p1 , p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                nums1.pop(p1)
                nums2.pop(p2)
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums2[p2] < nums1[p1]:
                p2 += 1
        return nums1, nums2


    # space: o(n), time: o(n)
    def findDifference_1(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # using dict
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        for k, v in c1.items():
            if v and c2.get(k):
                c1[k] = 0
                c2[k] = 0
        
        return [[k for k, v in c1.items() if v], [k for k, v in c2.items() if v]]

    def findDifference_2(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # using built-in methods
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]
    
    def findDifference_3(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # using set
        c1 = set(nums1)
        c2 = set(nums2)
        common = []
        # space: o(n), time: o(n)
        for k in c1:
            if k in c2:
                common.append(k)
        # time: o(n)
        for i in common:
            c1.remove(i)
            c2.remove(i)
        return c1, c2