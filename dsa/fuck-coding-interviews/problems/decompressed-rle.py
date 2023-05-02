# https://leetcode.com/problems/decompress-run-length-encoded-list/
from typing import List

class Solution:
    # Runtime: 135 ms, faster than 12.25% of Python3 online submissions for Decompress Run-Length Encoded List.
    # Memory Usage: 14.4 MB, less than 77.88% of Python3 online submissions for Decompress Run-Length Encoded List.
    # time Complexity: O(n/2) and space Complexity: O(n)
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        len_nums = len(nums)
        for i in range(len_nums//2):
            result += [nums[i+i+1]] * nums[i+i]
        return result
        