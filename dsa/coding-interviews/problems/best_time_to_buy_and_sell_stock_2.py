# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/

from typing import List


class Solution:
    """
    time: o(n)
    space: o(1)
    Runtime: 57 ms, faster than 98.88% of Python3 online submissions for Best Time to Buy and Sell Stock II.
    Memory Usage: 15.1 MB, less than 69.31% of Python3 online submissions for Best Time to Buy and Sell Stock II.
    """
    def maxProfit(self, prices: List[int]) -> int:
        # pattern find range where numbers are increasing
        max_profit = 0
        min_price = prices[0]
        max_price = prices[0]
        
        for i in range(1,len(prices)):
            # if prices are decreasing. sell current stock and buy it again.
            if not (max_price <= prices[i]):
                max_profit += max_price-min_price
                # start a new buying 
                min_price = prices[i]
            max_price = prices[i]
        max_profit += max_price-min_price
        return max_profit