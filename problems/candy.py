# https://leetcode.com/problems/candy/

from typing import List


class Solution:
    # time: o(2n), space: o(n)
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1] * n
        for index, rating in enumerate(ratings):
            if index -1 >=0 and ratings[index] > ratings[index-1]:
                res[index] = max(res[index], res[index-1] +1)
            if index + 1 < n and ratings[index] > ratings[index+1]:
                # backtrack changes..
                res[index] = max(res[index], res[index+1] +1)
        
        res_count = 0
        for index in range(n-1, -1, -1):
            if index + 1 < n and ratings[index] > ratings[index+1]:
                # backtrack changes..
                res[index] = max(res[index], res[index+1] +1)
            if index -1 >=0 and ratings[index] > ratings[index-1]:
                res[index] = max(res[index], res[index-1] +1)
            res_count += res[index]

        return res_count