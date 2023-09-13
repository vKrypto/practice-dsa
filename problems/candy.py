# https://leetcode.com/problems/candy/

from typing import List


class Solution:
    # time: o(2n), space: o(n)
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1] * n
        
        # from start to end
        for i in range(n-1):
            if ratings[i] < ratings[i+1]:
                res[i+1] = max(1 + res[i], res[i+1])
        
        res_count = res[-1]
        for i in range(n-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                res[i] = max(1 + res[i+1], res[i])
            res_count += res[i]
            
        return res_count