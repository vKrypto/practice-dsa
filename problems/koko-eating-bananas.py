# https://leetcode.com/problems/koko-eating-bananas/


import math
from typinf import List

class Solution:

    # time: O(logn), space = O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_koko_can_eat_pile(k):
            total_time_taken = sum([math.ceil(pile/k) for pile in piles])
            return total_time_taken <= h

        left, right = 1, max(piles)

        min_k = right
        # run binary loop, and check if koko can eat pile in h hours or not ?
        while left <= right:
            mid = (left+ right)//2
            if is_koko_can_eat_pile(mid):
                # print("can finish for ", mid)
                min_k = min(min_k, mid) # min is un-nceessary
                right = mid-1
            else:
                # print("can not finish for ", mid)
                left = mid + 1
        
        return min_k