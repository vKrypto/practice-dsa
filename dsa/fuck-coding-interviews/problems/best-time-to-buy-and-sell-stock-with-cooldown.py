# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/submissions/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}

        def rec(i=0, buy=None):
            if i >= len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i,buy)]        

            if buy is None:
                # buy or not buy
                case_1 = rec(i+1, buy=prices[i])
                case_2 = rec(i+1)
            else:
                # sell or not sell..
                case_1 = prices[i] - buy + rec(i+2)
                case_2 = rec(i+1, buy=buy)

            dp[(i,buy)] = max(case_1, case_2)
            return max(case_1, case_2)
            
        return rec()