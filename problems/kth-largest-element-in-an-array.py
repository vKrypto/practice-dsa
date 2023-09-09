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
class Solution:
    def partition(self, nums: List[int], left: int, last: int) -> int:
        pivot = nums[last]

        for right in range(left, last):
            if nums[right] <= pivot:
                if right != left:
                    nums[left], nums[right] = nums[right], nums[left]
                left += 1

        nums[left], nums[last] = nums[last], nums[left]

        return left

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