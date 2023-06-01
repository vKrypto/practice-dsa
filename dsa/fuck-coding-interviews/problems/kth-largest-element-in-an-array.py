# coding: utf-8
"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
from typing import List
import heapq


class Solution:
    # time: o(nlogn), space: o(1)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        return sorted_nums[len(sorted_nums) - k]


class Solution2:
    # time= o((n+k)logn) # space: o(n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        # o(n)
        for num in nums:
            # o(log(n))
            heapq.heappush(max_heap, -num)

        kth_largest = None
        # o(k)
        for _ in range(k):
            # o(log(n))))
            kth_largest = heapq.heappop(max_heap)
        return -kth_largest


class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_largests = heapq.nlargest(k, nums)
        return k_largests[-1]
