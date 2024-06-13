# coding: utf-8
"""
https://leetcode.com/problems/permutations/
"""
from typing import List
import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return itertools.permutations(nums)


    def permute_1(self, nums: List[int]) -> List[List[int]]:
        def permutations(elements):
            if len(elements) <= 1:
                yield elements  # elements is a list.
            else:
                for i, first in enumerate(elements):
                    other_elements = elements[:i] + elements[i + 1:]
                    for permutation in permutations(other_elements):
                        yield [first, ] + permutation

        return permutations(nums)

    # nums: variable to backtrack
    def permute_2(self, nums: List[int]) -> List[List[int]]:
        stack = []
        visited = [False] * len(nums)
        res=[]
        def backtrack(i=0):
            if len(stack) == len(nums):
                res.append(stack[::])
                return
            
            for j, num in enumerate(nums):
                if not visited[j]:
                    visited[j] = True
                    stack.append(num)
                    backtrack(i+1)
                    stack.pop()
                    visited[j] = False

        backtrack(0)
        return res

    # nums: variable to backtrack
    def permute_3(self, nums: List[int]) -> List[List[int]]:
        res = []
        # base-case
        if len(nums) == 1:
            return [[nums[0]]]
        # do all the stuffs, explore all possible cases( split branch)
        for i in range(len(nums)):
            num = nums.pop(0) # pop one item
            res_i = self.permute(nums)
            nums.append(num) # add back

            # combine result to return.
            for res_index in range(len(res_i)):
                res_i[res_index].append(num)
            res.extend(res_i)

        return res