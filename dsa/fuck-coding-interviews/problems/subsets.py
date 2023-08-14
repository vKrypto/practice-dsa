from itertools import combinations
from typing import List


class Solution:

    def subsets_1(self, nums: List[int]) -> List[List[int]]:
        # bottom-up approach
        res = []
        subset = []

        def dfs(i):
            # i==> decision_index
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

    def subsets_2(self, nums: List[int]) -> List[List[int]]:
        # bit manipulation
        n = len(nums)
        result = []

        for i in range(2**n):
            subset = []
            for j in range(n):
                if (i >> j) & 1:
                    subset.append(nums[j])
            result.append(subset)

        return result

    """
    Runtime: 60 ms, faster than 49.80% of Python3 online submissions for Subsets.
    Memory Usage: 14 MB, less than 82.42% of Python3 online submissions for Subsets.
    """
    def subsets_3(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)+1):
            res += [list(x) for x in combinations(nums, i)]
        return res

    def subsets_4(self, nums: List[int]) -> List[List[int]]:
        # divide and conquer
        def sol(lst):
            if not lst:
                return [[]]
            else:
                x = sol(lst[1:])
                return x + [[lst[0]] + y for y in x]

        return sol(nums)

    def subsets_5(self, nums: List[int]) -> List[List[int]]:
        # top-bottom approach,
        res = []
        subset = []
        def dfs(i):
            # print("---" * (i+1), subset)
            if i == len(nums):
                res.append(subset.copy())
                return
            # Decision not to include nums[i]
            dfs(i + 1)
            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

        dfs(0)
        return res
