# https://leetcode.com/problems/predict-the-winner/
from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def func(i,j, a_turn=True):
            if i>j:
                return 0
            if a_turn:
                way_1 = nums[i] + func(i+1, j, not a_turn)
                way_2 = nums[j] + func(i, j-1, not a_turn)
                return max(way_1, way_2)
            else:
                way_1 = func(i+1, j, not a_turn)
                way_2 = func(i, j-1, not a_turn)
                return min(way_1, way_2)

        score_1 = func(0, len(nums)-1)
        return score_1  >= sum(nums)/2

