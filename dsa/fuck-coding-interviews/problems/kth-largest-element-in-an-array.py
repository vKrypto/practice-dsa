# coding: utf-8
"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
from typing import List
import heapq


class Solution:

    # time: o(nlogn), space: o(1)
    def findKthLargest_1(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        return sorted_nums[len(sorted_nums) - k]

    # time= o((n+k)logn) # space: o(n)
    def findKthLargest_2(self, nums: List[int], k: int) -> int:
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

    def findKthLargest_3(self, nums: List[int], k: int) -> int:
        k_largests = heapq.nlargest(k, nums)
        return k_largests[-1]


# Solution: QuickSelect
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)
class Solution2:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1

        nums[fill], nums[right] = nums[right], nums[fill]

        return fill

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        while left < right:
            pivot = self.partition(nums, left, right)

            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break

        return nums[k]
