# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:

    """
    bruteforce method
    time Complexity: O(n^2).
    space Complexity: O(1)
    Runtime: 150 ms, faster than 64.16% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
    Memory Usage: 14.9 MB, less than 90.22% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
    """
    def twoSumUnOptimed(self, numbers: List[int], target: int) -> List[int]:
        for i, v1 in enumerate(numbers):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            for j, v2 in enumerate(numbers[i+1:]):
                if v1 + v2 == target:
                    return [i+1,i +j+1+1]
        
    """
    time Complexity: O(n).
    space Complexity: O(1)
    Runtime: 118 ms, faster than 99.65% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
    Memory Usage: 14.9 MB, less than 90.22% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            temp = numbers[l] + numbers[r]
            if temp < target:
                l += 1
            if temp > target:
                r -= 1
            elif temp == target:
                return [l+1, r+1]
            